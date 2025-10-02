# Python temperature converter

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").upper().strip()
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = (9*temp)/5+32
    print(f"The temperature in Farenheit is: {temp:.2f}ºF")
elif unit == "F":
    temp = (temp - 32)*5/9
    print(f"The temperature in Celsius is: {temp:.2f}ºC")
else:
    print(f"{unit} is an invalid unit of measurement")