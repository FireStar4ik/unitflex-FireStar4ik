import sys
from uniflex.core import convert
def main():
    if len(sys.argv) != 5:
        print("Usage: python cli.py <domain> <from_unit> <to_unit> <value>")
        return
    domain , from_unit, to_unit, value = sys.argv[1:5]
    try:
        value = float(value)
        result = convert(domain, from_unit, to_unit, value)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()