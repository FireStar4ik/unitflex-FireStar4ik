import requests

DEFAULT_RATE_USD_TO_EUR = 0.94
DEFAULT_RATE_EUR_TO_USD = 1.06

API_KEY = "cd2d16ee2f90d8d0fc1f9f8b6e0bd2c6"

def get_fallback_rate(from_currency, to_currency):
    if from_currency.lower() == "usd" and to_currency.lower() == "eur":
        return DEFAULT_RATE_USD_TO_EUR
    elif from_currency.lower() == "eur" and to_currency.lower() == "usd":
        return DEFAULT_RATE_EUR_TO_USD
    else:
        raise ValueError("Unsupported currency conversion")

def get_live_rate(from_currency, to_currency):
    url = "https://api.exchangerate.host/convert"
    params = {
        "access_key": API_KEY,
        "from": from_currency.upper(),
        "to": to_currency.upper(),
        "amount": 1
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        if data.get("success"):
            return data.get("result", get_fallback_rate(from_currency, to_currency))
        else:
            print("API error:", data)
            return get_fallback_rate(from_currency, to_currency)
    except Exception as e:
        print("API exception:", e)
        return get_fallback_rate(from_currency, to_currency)

def convert_currency(from_unit, to_unit, value):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if (from_unit, to_unit) not in [("usd", "eur"), ("eur", "usd")]:
        raise ValueError("Unsupported currency units")

    rate = get_live_rate(from_unit, to_unit)
    return value * rate
