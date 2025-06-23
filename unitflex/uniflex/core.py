from . import temperature
from . import currency
from . import distance
def convert(domain: str, from_unit: str, to_unit: str, value: float) -> float:
    if domain == "temperature":
        if from_unit == "celsius" and to_unit == "fahrenheit":
            return temperature.ctof(value)
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            return temperature.ftoc(value)
        else:
            raise ValueError("Unsupported temperature conversion")
    elif domain == "currency":
        if from_unit == "dollar" and to_unit == "euro":
            return currency.dtoe(value)
        elif from_unit == "euro" and to_unit == "dollar":
            return currency.etod(value)
        else:
            raise ValueError("Unsupported currency conversion")
    elif domain == "distance":
        if from_unit == "km" and to_unit == "mile":
            return distance.kmtom(value)
        elif from_unit == "mile" and to_unit == "km":
            return distance.mtokm(value)
        else:
            raise ValueError("Unsupported distance conversion")
    else:
        raise ValueError("Unsupported domain")