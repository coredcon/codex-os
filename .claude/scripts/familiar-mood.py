"""
familiar-mood.py
Controls office Govee lights based on Desktop Familiar mood state.

Usage:
    python familiar-mood.py <mood>

Moods:
    idle      — passive, waiting         → River
    curious   — engaged, processing      → Awaken
    focused   — deep work / user working → Study
    playful   — light, conversational    → Happy
    sleepy    — dormant / late night     → Asleep
    alert     — attention needed         → Bright blue (custom RGB)
    campaign  — Pathfinder Sunday        → Candlelight

To add a DIY scene:
    1. Design in Govee app, note the name
    2. Run: python familiar-mood.py --list-diy
    3. Add the returned paramId/id to MOODS below
"""
import sys, json, urllib.request

API_KEY = "639456ea-7e6f-4a18-bba7-55cd39c22827"

DEVICES = [
    ("H6013", "CB:F6:DC:1E:D5:52:80:90"),  # Office 1
    ("H6013", "CE:8D:DC:06:75:48:40:0C"),  # Office 2
    ("H6013", "27:84:DC:06:75:45:8A:88"),  # Office 3
    ("H6013", "18:F9:DC:06:75:47:E4:68"),  # Office 4
]

MOODS = {
    "idle":     {"type": "scene", "scene": {"paramId": 1238, "id": 1176}},  # River
    "curious":  {"type": "scene", "scene": {"paramId": 1259, "id": 1197}},  # Awaken
    "focused":  {"type": "rgb", "rgb": 10506240},                           # dim amber rgb(160,90,0)
    "playful":  {"type": "scene", "scene": {"paramId": 3287, "id": 3137}},  # Happy
    "sleepy":   {"type": "scene", "scene": {"paramId": 1263, "id": 1201}},  # Asleep
    "alert":    {"type": "rgb",   "rgb": 38655},                            # rgb(0,150,255)
    "campaign": {"type": "scene", "scene": {"paramId": 3280, "id": 3130}},  # Candlelight
    # DIY slots — fill in after designing in Govee app
    # "diy_excited": {"type": "scene", "scene": {"paramId": ???, "id": ???}},
}


def build_capability(mood_config):
    if mood_config["type"] == "scene":
        return {
            "type": "devices.capabilities.dynamic_scene",
            "instance": "lightScene",
            "value": mood_config["scene"],
        }
    elif mood_config["type"] == "rgb":
        return {
            "type": "devices.capabilities.color_setting",
            "instance": "colorRgb",
            "value": mood_config["rgb"],
        }


def set_mood(mood):
    if mood not in MOODS:
        print(f"Unknown mood: '{mood}'. Available: {', '.join(MOODS)}")
        sys.exit(1)

    config = MOODS[mood]
    capability = build_capability(config)

    for sku, device in DEVICES:
        payload = json.dumps({
            "requestId": f"familiar-{mood}",
            "payload": {
                "sku": sku,
                "device": device,
                "capability": capability,
            }
        }).encode()
        req = urllib.request.Request(
            "https://openapi.api.govee.com/router/api/v1/device/control",
            data=payload,
            headers={"Govee-API-Key": API_KEY, "Content-Type": "application/json"},
            method="POST",
        )
        urllib.request.urlopen(req)

    print(f"Familiar mood: {mood}")


def list_diy():
    """Query and print all DIY scenes from your Govee account."""
    sku, device = DEVICES[0]
    url = f"https://openapi.api.govee.com/router/api/v1/device/diy-scenes?sku={sku}&device={device}"
    req = urllib.request.Request(
        url,
        headers={"Govee-API-Key": API_KEY},
        method="GET",
    )
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python familiar-mood.py <mood>")
        print(f"Moods: {', '.join(MOODS)}")
        print(f"       --list-diy   (show your DIY scenes)")
        sys.exit(1)

    if sys.argv[1] == "--list-diy":
        list_diy()
    else:
        set_mood(sys.argv[1])
