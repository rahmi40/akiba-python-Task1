celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print()
print(f"celsius: {celsius:g} °C")
print(f"fahrenheit: {fahrenheit:g} °F")
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_from_fahrenheit = (fahrenheit_input - 32) * 5 / 9
print(f"Celsius: {celsius_from_fahrenheit:g}°C")