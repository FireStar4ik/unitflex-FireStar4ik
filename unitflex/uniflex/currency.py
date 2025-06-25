import requests

API_KEY = 'cd2d16ee2f90d8d0fc1f9f8b6e0bd2c6'
DEFAULT_RATE = 0.9

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
            return data.get("result", DEFAULT_RATE)
        else:
            print("API error:", data)
            return DEFAULT_RATE
    except Exception as e:
        print("API ERROR:", e)
        return DEFAULT_RATE

def dtoe(amount):
    rate = get_live_rate("USD", "EUR")
    return amount * rate

def etod(amount):
    rate = get_live_rate("EUR", "USD")
    return amount * rate
