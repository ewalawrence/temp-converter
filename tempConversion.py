# Python Temp Conversion

temp = float(input("Enter the temprature: "))
unit = input("Is the unit in Fahrenheit or Celsius (F or C): ").upper()

if unit == "F":
    result = round((temp - 32) * 5 / 9, 1)
    print(f"The new converted temperature is {result}°C")
elif unit == "C":
    result = round((9/5 * temp) + 32, 1)
    print(f"The new converted temperature is {result}°F")
else:
    print(f"The {unit} you entered is invalid")
