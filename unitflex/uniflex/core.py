from uniflex.currency import dtoe, etod
from uniflex.temperature import ctof, ftoc
from uniflex.distance import kmtom, mtokm

def convert(domain: str, from_unit: str, to_unit: str, value: float) -> float:
    domain = domain.lower()
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    print(f"[DEBUG] domain={domain}, from={from_unit}, to={to_unit}")

    if domain == "temperature":
        if from_unit == "celsius" and to_unit == "fahrenheit":
            return ctof(value)
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            return ftoc(value)

    elif domain == "distance":
        if from_unit == "kilometers" and to_unit == "miles":
            return kmtom(value)
        elif from_unit == "miles" and to_unit == "kilometers":
            return mtokm(value)

    elif domain == "currency":
        if from_unit == "usd" and to_unit == "eur":
            return dtoe(value)
        elif from_unit == "eur" and to_unit == "usd":
            return etod(value)
        else:
            raise ValueError(f"Unsupported currency conversion: {from_unit} → {to_unit}")


    print(f"Got: domain={domain}, from={from_unit}, to={to_unit}")
    raise ValueError("Unsupported conversion")


