"""Query Govee API for all available dynamic scenes on the device."""
import urllib.request, json

API_KEY = "639456ea-7e6f-4a18-bba7-55cd39c22827"
SKU = "H6013"
DEVICE = "CB:F6:DC:1E:D5:52:80:90"  # Office 1

payload = json.dumps({
    "requestId": "list-scenes",
    "payload": {"sku": SKU, "device": DEVICE}
}).encode()

req = urllib.request.Request(
    "https://openapi.api.govee.com/router/api/v1/device/scenes",
    data=payload,
    headers={"Govee-API-Key": API_KEY, "Content-Type": "application/json"},
    method="POST",
)
resp = urllib.request.urlopen(req)
data = json.loads(resp.read())
print(json.dumps(data, indent=2))
