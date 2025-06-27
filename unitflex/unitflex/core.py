from unitflex.temperature import convert_temperature
from unitflex.distance import convert_distance
from unitflex.currency import convert_currency

def convert(domain: str, from_unit: str, to_unit: str, value: float) -> float:
    domain = domain.lower()

    if domain == "temperature":
        return convert_temperature(from_unit.lower(), to_unit.lower(), value)
    elif domain == "distance":
        return convert_distance(from_unit.lower(), to_unit.lower(), value)
    elif domain == "currency":
        return convert_currency(from_unit.lower(), to_unit.lower(), value)
    else:
        raise ValueError(f"Unsupported domain: {domain}")
