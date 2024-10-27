# °C , °F , K , Rn , R , °R

import time

while True:
    unit = input("Enter the unit of temperature whose data you have: ")
    if unit.upper() in ["°C", "°F", "°R", "C", "F", "R", "Rn", "K"]:
        while True:
            try:
                value = float(input("Enter the magnitude of the temperature: "))
                break
            except :
                print("The code understands string as an invalid input. Please enter a numeric value of the temperature")
            # The inner while loop is a must. try and except should always have a loop running otherwise if value is entered incorrect then error will occur outside

    # When the try block raises an exception, it skips the break and jumps directly to the except block. The loop then continues to ask for input. If the try block succeeds, the break executes, and the loop exits. It's a graceful way to handle errors and keep the flow going smoothly. We need break to exit or else it will ask for magnitude of temperature again. Break needs to be inside of the try block and not inside the except block

    else:
        print(f"This code doesn't understand {unit} temperature unit.")
        continue # Prompt to unit again if invalid

    print(f"You have entered {value}{unit}")

    again = input("Do you wish to change the given temperature value and the unit? (yes/no) : ")

    if again.lower() == "no":
        break
    
while True:
    convert = input(f"Enter the unit of temperature that you wish to convert {value}{unit} into : ")
    if convert.upper() not in ["°C", "°F", "°R", "C", "F", "R", "Rn", "K"]:
        print(f"This code doesn't understand {convert} temperature unit.")
        convert = input("Enter the unit of temperature among °C , °F , K , Rn , R , °R : ")
    else:
        print("Give me a second here.")
        time.sleep(1)
        print("Performing calculations")
        time.sleep(1)
        for i in range (1,4):
            print("." , end = " ",flush = True )
            time.sleep(1)
        break

# so basically flush = True makes python to stop optimizing performance and show real time effects


print()
if unit.upper() == "Rn":
    celsius = (value - 491.67) / 1.8
elif unit.upper() in ["°F", "F"]:
    celsius = (value - 32) / 1.8
elif unit.upper() == "K":
    celsius = value - 273.15
elif unit.upper() in ["°R", "R"]:
    celsius = value / 0.8
else:
    celsius = value

if convert.upper() == "Rn":
    temp = (1.8 * celsius) + 491.67
elif convert.upper() in ["°F", "F"]:
    temp = (1.8 * celsius) + 32
elif convert.upper() == "K":
    temp = celsius + 273.15
elif convert.upper() in ["°R", "R"]:
    temp = 0.8 * celsius
else:
    temp = celsius

print(f"The required temperature is {temp} {convert}")


# try block: You put the code that might cause an error in here. If an error occurs, it jumps to the except block.

# except block: This code runs if there’s an error in the try block. It’s your safety net to handle the error gracefully instead of crashing your program.


# break stops the loop entirely, while continue just jumps to the next iteration. If continue is used on the last iteration, the loop naturally ends afterward.