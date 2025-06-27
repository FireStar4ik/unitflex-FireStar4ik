def convert_distance(from_unit, to_unit, value):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == "kilometers" and to_unit == "miles":
        return value * 0.62138   
    elif from_unit == "miles" and to_unit == "kilometers":
        return value * 1.6093
    else:
        raise ValueError("Unsupported distance units")
