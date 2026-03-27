#!/usr/bin/env python3
"""
Vox Job Search — automated job listing scanner
Sources: RemoteOK API (no-auth, free), We Work Remotely RSS
Indeed: handled separately via Indeed MCP (Claude-side)
Deduplicates, logs new finds to vault tracker
"""

import json
import os
import sys
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime
import re
import html

# Force UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── Config ──────────────────────────────────────────────────────────────────

VAULT_ROOT   = "F:/My Drive/Obsidian/Codex.os"
TRACKER_FILE = f"{VAULT_ROOT}/05 Areas/Career/job-tracker.md"
SEEN_FILE    = f"{VAULT_ROOT}/05 Areas/Career/.job-seen.json"

# RemoteOK tags to search (https://remoteok.io/api?tag=TAG)
REMOTEOK_TAGS = [
    ("solutions-engineer",  "Solutions Engineer"),
    ("account-manager",     "Technical Account Manager"),
    ("technical",           "Technical Roles"),
    ("saas",                "SaaS"),
    ("api",                 "API/Integration"),
]

# We Work Remotely RSS categories
WWR_FEEDS = [
    ("https://weworkremotely.com/categories/remote-customer-support-jobs.rss",    "Customer/Technical Support"),
    ("https://weworkremotely.com/categories/remote-sales-and-marketing-jobs.rss", "Sales/Solutions"),
    ("https://weworkremotely.com/categories/remote-full-stack-programming-jobs.rss", "Technical/Engineering"),
]

# Title must contain at least one of these (case-insensitive)
INCLUDE_TITLE_KEYWORDS = [
    "solutions engineer",
    "technical account manager",
    "pre-sales engineer",
    "presales engineer",
    "integration specialist",
    "implementation specialist",
    "implementation engineer",
    "technical program manager",
    "technical project manager",
    "technical support engineer",
    "support engineer",
    "api specialist",
    "api engineer",
    "automation specialist",
    "ai specialist",
    "customer success engineer",
    "technical customer success",
    "saas configuration",
    "platform specialist",
    "technical consultant",
    "senior technical analyst",
    "escalation engineer",
]

# Skip if title contains any of these (case-insensitive)
EXCLUDE_TITLE_KEYWORDS = [
    "staffing", "recruiter", "sales representative", "account executive",
    "clearance", "director", "vice president", "vp ", "chief",
    "data scientist", "machine learning", "software engineer", "frontend",
    "backend", "devops", "cloud architect", "security architect",
    "brand designer", "designer", "accountant", "finance", "legal",
    "hr ", "human resources", "marketing", "product manager",
    "business development", "channel manager",
]

# ── Helpers ──────────────────────────────────────────────────────────────────

def load_seen():
    if os.path.exists(SEEN_FILE):
        with open(SEEN_FILE, "r") as f:
            return set(json.load(f))
    return set()

def save_seen(seen):
    os.makedirs(os.path.dirname(SEEN_FILE), exist_ok=True)
    with open(SEEN_FILE, "w") as f:
        json.dump(sorted(seen), f)

def clean_html(text):
    text = html.unescape(text or "")
    text = re.sub(r"<[^>]+>", "", text)
    return " ".join(text.split()).strip()

def is_good_match(title, description=""):
    t = title.lower()
    if any(kw in t for kw in EXCLUDE_TITLE_KEYWORDS):
        return False
    return any(kw in t for kw in INCLUDE_TITLE_KEYWORDS)

def fetch_url(url, headers=None):
    h = {"User-Agent": "Mozilla/5.0 (compatible; VoxJobBot/1.0)"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read()

# ── Sources ───────────────────────────────────────────────────────────────────

def search_remoteok(tag, label):
    """Fetch from RemoteOK API."""
    url = f"https://remoteok.io/api?tag={urllib.parse.quote(tag)}"
    try:
        raw = fetch_url(url, {"Accept": "application/json"})
        data = json.loads(raw)
    except Exception as e:
        return [], f"RemoteOK ({tag}): {e}"

    jobs = []
    for item in data:
        if not isinstance(item, dict) or "position" not in item:
            continue
        title    = item.get("position", "")
        company  = item.get("company", "Unknown")
        location = item.get("location", "Remote")
        link     = item.get("url", f"https://remoteok.io/jobs/{item.get('id', '')}")
        tags     = " ".join(item.get("tags", []))
        guid     = item.get("id", link)
        snippet  = clean_html(item.get("description", ""))[:200]

        if not is_good_match(title, tags + " " + snippet):
            continue

        jobs.append({
            "guid": str(guid), "title": title, "company": company,
            "location": location or "Remote", "link": link, "snippet": snippet,
        })

    return jobs, None

def search_wwr(feed_url, label):
    """Fetch from We Work Remotely RSS."""
    try:
        raw = fetch_url(feed_url)
        root = ET.fromstring(raw)
    except Exception as e:
        return [], f"WWR ({label}): {e}"

    jobs = []
    channel = root.find("channel")
    if not channel:
        return [], None

    for item in channel.findall("item"):
        title   = clean_html(item.findtext("title", ""))
        company = ""
        # WWR title format: "Company: Job Title"
        if ": " in title:
            company, title = title.split(": ", 1)
        link    = item.findtext("link", "").strip()
        guid    = item.findtext("guid", link).strip()
        snippet = clean_html(item.findtext("description", ""))[:200]

        if not is_good_match(title, snippet):
            continue

        jobs.append({
            "guid": guid, "title": title, "company": company,
            "location": "Remote", "link": link, "snippet": snippet,
        })

    return jobs, None

# ── Tracker ───────────────────────────────────────────────────────────────────

def ensure_tracker():
    os.makedirs(os.path.dirname(TRACKER_FILE), exist_ok=True)
    if not os.path.exists(TRACKER_FILE):
        with open(TRACKER_FILE, "w", encoding="utf-8") as f:
            f.write("# Job Tracker\n\n> Auto-updated by Vox — `job-search.py`\n> Roles: Solutions Engineer, TAM, Pre-Sales, Integration Specialist, AI/Automation\n\n---\n\n")

def append_jobs_to_tracker(new_jobs_by_label):
    ensure_tracker()
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    total = sum(len(j) for j in new_jobs_by_label.values())
    lines = [f"\n## Scan — {today}  ({total} new)\n"]

    for label, jobs in new_jobs_by_label.items():
        if not jobs:
            continue
        lines.append(f"\n### {label}\n")
        for j in jobs:
            lines.append(f"- **[{j['title']}]({j['link']})** — {j['company']} | {j['location']}")
            if j["snippet"]:
                lines.append(f"  > {j['snippet'][:180]}")
            lines.append("")

    with open(TRACKER_FILE, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    seen     = load_seen()
    new_seen = set()
    results  = {}
    errors   = []

    # RemoteOK
    for tag, label in REMOTEOK_TAGS:
        jobs, err = search_remoteok(tag, label)
        if err:
            errors.append(err)
        fresh = [j for j in jobs if j["guid"] not in seen and j["guid"] not in new_seen]
        for j in fresh:
            new_seen.add(j["guid"])
        key = f"RemoteOK — {label}"
        results[key] = results.get(key, []) + fresh

    # We Work Remotely
    for url, label in WWR_FEEDS:
        jobs, err = search_wwr(url, label)
        if err:
            errors.append(err)
        fresh = [j for j in jobs if j["guid"] not in seen and j["guid"] not in new_seen]
        for j in fresh:
            new_seen.add(j["guid"])
        key = f"WWR — {label}"
        results[key] = results.get(key, []) + fresh

    total_new = sum(len(v) for v in results.values())

    if total_new > 0:
        append_jobs_to_tracker(results)
        save_seen(seen | new_seen)
        print(f"[JOB SEARCH] {total_new} new listing(s) found -- see Career/job-tracker.md")
        for label, jobs in results.items():
            if jobs:
                print(f"  {label}: {len(jobs)} new")
    else:
        save_seen(seen | new_seen)
        print("[JOB SEARCH] No new listings since last scan.")

    for e in errors:
        print(f"  WARNING: {e}")

if __name__ == "__main__":
    main()
