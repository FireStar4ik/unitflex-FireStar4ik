import urllib.request
import json

DEFAULT_RATE = 0.9
API_KEY = "cd2d16ee2f90d8d0fc1f9f8b6e0bd2c6"

def get_live_rate(from_unit: str, to_unit: str) -> float:
    url = f"https://api.exchangerate.host/convert?from={from_unit}&to={to_unit}&api_key={API_KEY}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read())
            print("DEBUG: API response =", data)
            return data.get("result", DEFAULT_RATE)
    except Exception as e:
        print("API ERROR:", e)
        return DEFAULT_RATE

def dtoe(amount):
    rate = get_live_rate("USD", "EUR")
    return amount * rate

def etod(amount):
    rate = get_live_rate("EUR", "USD")
    return amount * rate
