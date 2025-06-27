import sys
from unitflex import convert


if __name__ == "__main__":
    domain, from_unit, to_unit, value = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4])
    
    try:
        result = convert(domain, from_unit, to_unit, value)
        print(f"{value} {from_unit} = {result:.2f} {to_unit}")
    except Exception as e:
        print(f"Error: {e}")
