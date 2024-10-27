# input() = A function that prompts the user to enter data and returns the input data the user inputs as a string

name = input("What is your name?: ") # What is your name will be displayed in the output and the input function asks for
# an input from the user.
age = int(input("How old are you ?")) # Int is necessary for the condition else it wasn't necessary


print(f"Hello {name}!")
# Because of this line we have to use int in the age because the input is string
if age == 35: # To compare variables we use == for all cases.
  print(f"So you're {age} years old, huh!")
elif 30 <= age < 35:
  print("Well you are getting old.")
else:
  print(f"What's a {age} old doing here?")

# So we need to make the interpreter clear to understand what is going on here. Indentation (space) also plays a crucial
# role here. For eg:
# print(f"Hello {name}!")
# if age <= 35:
# print(f"So you're {age} years old, huh!") *******(Gap must be given here)
# else:
# print(f"What's {age} old boomer doing here?") *******(Gap must be given here)

#This is wrong because we didn't give spaces for the print of if and else