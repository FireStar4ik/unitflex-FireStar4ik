def convert_temperature(from_unit, to_unit, value):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    else:
        raise ValueError(f"Unsupported temperature conversion: {from_unit} to {to_unit}")
