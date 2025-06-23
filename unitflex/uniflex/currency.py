import urllib.request
import json

DEFAULT_RATE = 0.9

def get_rate(from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            return data['rates'].get(to_currency, DEFAULT_RATE)
    except Exception:
        return DEFAULT_RATE