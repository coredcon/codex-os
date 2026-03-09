"""
govee-campaign-mode.py
Sets office lights to Candlelight (campaign mode) via Govee API.
Triggered automatically by Windows Task Scheduler every Sunday at 3pm.
"""
import urllib.request, json

API_KEY = "639456ea-7e6f-4a18-bba7-55cd39c22827"
DEVICES = [
    ("H6013", "CB:F6:DC:1E:D5:52:80:90"),
    ("H6013", "CE:8D:DC:06:75:48:40:0C"),
    ("H6013", "27:84:DC:06:75:45:8A:88"),
    ("H6013", "18:F9:DC:06:75:47:E4:68"),
]
CANDLELIGHT = {"paramId": 3280, "id": 3130}

for sku, device in DEVICES:
    payload = json.dumps({
        "requestId": "campaign",
        "payload": {
            "sku": sku,
            "device": device,
            "capability": {
                "type": "devices.capabilities.dynamic_scene",
                "instance": "lightScene",
                "value": CANDLELIGHT
            }
        }
    }).encode()
    req = urllib.request.Request(
        "https://openapi.api.govee.com/router/api/v1/device/control",
        data=payload,
        headers={"Govee-API-Key": API_KEY, "Content-Type": "application/json"},
        method="POST"
    )
    urllib.request.urlopen(req)

print("Campaign mode set — Candlelight active.")
