
# # unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")


# # if unit == "C" :
# #     temp = float(input("Enter the temperature: "))
# #     temp = round((temp * 1.8) + 32)
# #     print(f"The temperature in Fahrenheit is {temp} °F")
# # elif unit == "F" :
# #     temp = float(input("Enter the temperature: "))
# #     temp = round((temp-32)/1.8)
# #     print(f"The temperature in Celsius is {temp} °C")
# # else :
# #     print(f"The given unit i.e. {unit} is an invalid one for the operator.")


unit = input("Enter the unit of temperature that you have: (°C/°F/K/Rn/°Ré) ")
temp = float(input("Enter the magnitude of the temperature: "))
convert = input(f"Enter the unit of temperature that you want it to convert into (°C/°F/K/Rn/°Ré) except {unit} obviously: ") 

if unit.upper() == "°C" or unit.upper() == "C": # Conditions with or need to be stated explicitly
    if convert.upper() == "°F" or convert.upper() == "F":
        result = round((temp * 1.8) + 32 , 2)
    elif convert.upper() == "K":
        result = round(temp + 273 , 2)
    elif convert == "Rn":
        result = round((temp * 1.8) + 492 , 2)
    elif convert.upper() in ["°RÉ", "°RE", "RÉ", "RE", "°R", "R"]:
        result = round(temp * 0.8)

elif unit.upper() == "°F" or unit.upper() == "F":
    if convert.upper() == "°C" or convert.upper() == "C":
        result = round((temp-32)/1.8 , 2)
    elif convert.upper() == "K":
        result = round((temp-32)/1.8 + 273 , 2)
    elif convert == "Rn":
        result = round((temp + 460) , 2)
    elif convert.upper() in ["°RÉ", "°RE", "RÉ", "RE", "°R", "R"]: 
    # Ctrl C on the blank line or a line without highlighting anything copies that entire line.
        result = round((temp-32)/2.25 , 2)


elif unit.upper() == "K":
    if convert.upper() == "°C" or convert.upper() == "C":
        result = round(temp - 273 , 2)
    elif convert.upper() == "°F" or convert.upper() == "F":
        result = round(1.8 * (temp - 273) + 32 , 2)
    elif convert == "Rn":
        result = round(1.8 * (temp - 273) + 492 , 2)
    elif convert.upper() in ["°RÉ", "°RE", "RÉ", "RE", "°R", "R"]: 
        result = round(0.8 * (temp - 273))
    else: 
        print("Invalid user input")


elif unit == "Rn":
    if convert.upper() == "°C" or convert.upper() == "C":
        result = round((temp - 492)/1.8 , 2)
    elif convert.upper() == "°F" or convert.upper() == "F":
        result = round(temp - 460 , 2)
    elif convert.upper() == "K":
        result = round((temp - 492)/1.8 + 273 , 2)
    elif convert.upper() in ["°RÉ", "°RE", "RÉ", "RE", "°R", "R"]:
        result = round((temp-492)/2.25 , 2)
    else: 
        print("Invalid user input")

elif unit.upper() in ["°RÉ", "°RE", "RÉ", "RE", "°R", "R"]:
    if convert.upper() == "°C" or convert.upper() == "C":
        result = round(temp/0.8 , 2)
    elif convert.upper() == "°F" or convert.upper() == "F":
        result = round((2.25 * temp) + 32 , 2)
    elif convert.upper() == "K":
        result = round((temp / 0.8) + 273 , 2)
    elif convert == "Rn" :
        result = round((2.25 * temp) + 492)
    else: 
        print("Invalid user input") 
       

else: 
    print("Invalid user input")

print(f"The temperature is {result}{convert}")
# Ctrl + enter opens a python REPL that executes

unit = input("Enter the unit of temperature that you have: (°C/°F/K/Rn/°Ré) ")
temp = float(input("Enter the magnitude of the temperature: "))
convert = input(f"Enter the unit of temperature that you want it to convert into (°C/°F/K/Rn/°Ré) except {unit} obviously: ")

if unit.upper() in ["°C", "C"]:
    if convert.upper() in ["°F", "F"]:
        result = round((temp * 1.8) + 32, 2)
    elif convert.upper() == "K":
        result = round(temp + 273.15, 2)
    elif convert == "Rn":
        result = round((temp * 1.8) + 491.67, 2)
    elif convert.upper() in ["°RÉ", "°RE", "RÉ", "RE", "°R", "R"]: # This acts as an or operator. Careful with in there. I gave == and error popped up and it took me a whole day.
        result = round(temp * 0.8, 2)
    else:
        result = "Invalid conversion unit."

elif unit.upper() in ["°F", "F"]:
    if convert.upper() in ["°C", "C"]:
        result = round((temp - 32) / 1.8, 2)
    elif convert.upper() == "K":
        result = round((temp - 32) / 1.8 + 273.15, 2)
    elif convert == "Rn":
        result = round(temp + 459.67, 2)
    elif convert.upper() in ["°RÉ", "°RE", "RÉ", "RE", "°R", "R"]:
        result = round((temp - 32) / 2.25, 2)
    else:
        result = "Invalid conversion unit."

elif unit.upper() == "K":
    if convert.upper() in ["°C", "C"]:
        result = round(temp - 273.15, 2)
    elif convert.upper() in ["°F", "F"]:
        result = round(1.8 * (temp - 273.15) + 32, 2)
    elif convert == "Rn":
        result = round(1.8 * (temp - 273.15) + 491.67, 2)
    elif convert.upper() in ["°RÉ", "°RE", "RÉ", "RE", "°R", "R"]:
        result = round(0.8 * (temp - 273.15), 2)
    else:
        result = "Invalid conversion unit."

elif unit == "Rn":
    if convert.upper() in ["°C", "C"]:
        result = round((temp - 491.67) / 1.8, 2)
    elif convert.upper() in ["°F", "F"]:
        result = round(temp - 459.67, 2)
    elif convert.upper() == "K":
        result = round((temp - 491.67) / 1.8 + 273.15, 2)
    elif convert.upper() in ["°RÉ", "°RE", "RÉ", "RE", "°R", "R"]:
        result = round((temp - 491.67) / 2.25, 2)
    else:
        result = "Invalid conversion unit."

elif unit.upper() in ["°RÉ", "°RE", "RÉ", "RE", "°R", "R"]:
    if convert.upper() in ["°C", "C"]:
        result = round(temp / 0.8, 2)
    elif convert.upper() in ["°F", "F"]:
        result = round((2.25 * temp) + 32, 2)
    elif convert.upper() == "K":
        result = round((temp / 0.8) + 273.15, 2)
    elif convert == "Rn":
        result = round((2.25 * temp) + 491.67, 2)
    else:
        result = "Invalid conversion unit."

else:
    result = "Invalid input or conversion unit."

print(f"The temperature is {result} {convert}")
