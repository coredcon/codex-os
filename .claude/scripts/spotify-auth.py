#!/usr/bin/env python3
"""
spotify-auth.py — One-time Spotify OAuth setup for Vox Watcher

Uses PKCE flow (no client secret needed).
Run this once to authorize and store refresh token.
After that, vox-watcher.py handles token refresh automatically.

Usage: python spotify-auth.py
"""

import base64
import hashlib
import http.server
import json
import os
import random
import secrets
import string
import threading
import urllib.parse
import urllib.request
import webbrowser
from datetime import datetime

CLIENT_ID = "fcd51263339842ffa8a6e6e2beb1847a"
REDIRECT_URI = "http://127.0.0.1:8888/callback"
SCOPES = "user-read-currently-playing user-read-playback-state user-modify-playback-state"
TOKEN_FILE = os.path.join(os.path.dirname(__file__), "spotify-token.json")
PORT = 8888

# --- PKCE helpers ---

def generate_code_verifier():
    chars = string.ascii_letters + string.digits + "-._~"
    return "".join(secrets.choice(chars) for _ in range(128))

def generate_code_challenge(verifier):
    digest = hashlib.sha256(verifier.encode()).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode()

def build_auth_url(verifier):
    challenge = generate_code_challenge(verifier)
    state = secrets.token_hex(8)
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPES,
        "code_challenge_method": "S256",
        "code_challenge": challenge,
        "state": state,
    }
    return "https://accounts.spotify.com/authorize?" + urllib.parse.urlencode(params), state

def exchange_code(code, verifier):
    data = urllib.parse.urlencode({
        "client_id": CLIENT_ID,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "code_verifier": verifier,
    }).encode()
    req = urllib.request.Request(
        "https://accounts.spotify.com/api/token",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

def save_tokens(token_data):
    to_save = {
        "access_token": token_data["access_token"],
        "refresh_token": token_data["refresh_token"],
        "expires_in": token_data["expires_in"],
        "saved_at": datetime.now().isoformat(),
    }
    with open(TOKEN_FILE, "w") as f:
        json.dump(to_save, f, indent=2)
    print(f"Tokens saved to {TOKEN_FILE}")

# --- Local callback server ---

class CallbackHandler(http.server.BaseHTTPRequestHandler):
    auth_code = None
    error = None

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        if "code" in params:
            CallbackHandler.auth_code = params["code"][0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"""
                <html><body style="font-family:sans-serif;padding:40px;text-align:center">
                <h2>Vox authorized!</h2>
                <p>You can close this window and return to the terminal.</p>
                </body></html>
            """)
        elif "error" in params:
            CallbackHandler.error = params["error"][0]
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Authorization denied.")
        else:
            self.send_response(400)
            self.end_headers()

    def log_message(self, *args):
        pass  # suppress server logs


def main():
    verifier = generate_code_verifier()
    auth_url, state = build_auth_url(verifier)

    print("\nVox Spotify Auth")
    print("=" * 40)
    print("Opening your browser to authorize Spotify...")
    print(f"\nIf it doesn't open, visit:\n{auth_url}\n")

    # Start local server to catch callback
    server = http.server.HTTPServer(("127.0.0.1", PORT), CallbackHandler)
    server_thread = threading.Thread(target=server.handle_request)
    server_thread.daemon = True
    server_thread.start()

    webbrowser.open(auth_url)
    server_thread.join(timeout=120)

    if CallbackHandler.error:
        print(f"Authorization error: {CallbackHandler.error}")
        return

    if not CallbackHandler.auth_code:
        print("Timed out waiting for authorization. Try again.")
        return

    print("Got authorization code — exchanging for tokens...")
    try:
        token_data = exchange_code(CallbackHandler.auth_code, verifier)
        save_tokens(token_data)
        print("\nSuccess! Vox Watcher can now use the Spotify API.")
        print("Run vox-watcher.py to start monitoring.")
    except Exception as e:
        print(f"Token exchange failed: {e}")


if __name__ == "__main__":
    main()
