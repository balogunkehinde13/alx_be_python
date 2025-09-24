# 🌡️ Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# 🔄 Conversion Functions
def convert_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# 🖥️ User Interaction
def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        if not temp_input.replace(".", "", 1).isdigit() and not (temp_input.startswith('-') and temp_input[1:].replace(".", "", 1).isdigit()):
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(temp_input)
        scale = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()

        if scale == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted:.2f}°F")
        elif scale == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted:.2f}°C")
        else:
            raise ValueError("Invalid input. Please specify 'C' or 'F'.")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
