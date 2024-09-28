# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit: Temperature in Fahrenheit (float).

    Returns:
        Temperature in Celsius (float).
    """
    return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit.

    Args:
        celsius: Temperature in Celsius (float).

    Returns:
        Temperature in Fahrenheit (float).
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR


def main():
    """Prompts user for temperature, converts it based on unit, and displays result."""
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input(
                "Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

            if unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)
                unit_label = "°C"
                result_unit = "°F"
            elif unit == 'F':
                converted_temp = convert_to_celsius(temperature)
                unit_label = "°F"
                result_unit = "°C"
            else:
                raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

            print(f"{temperature}{unit_label} is {
                  converted_temp:.2f}{result_unit}")
            break
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
