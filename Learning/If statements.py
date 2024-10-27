# # if = Do something if something is true else do something else

# age = int(input("Enter your age: "))

# if 18 <= age < 100: # To stop overwriting by unnecessary codes.
# #I should either change the order or change the code
#     print("You can now sign up")

# elif 10 >= age >= 1: # previously I just wrote age <= 10. It didn't let me run the below code
#     print("Are you kidding me 🤣🤣🤣. Do you even know what a credit card is?")

# elif age <= 0:
#     print("Bombastic side eye. Criminal offensive side eye.")

# elif age >= 100:
#     print("You're too old to sign up. Don't you think?")

# else :
#     print(f"Your credit card cannot be made because you're {age} years old. You must be 18 years old or older but not too old.")


# # Response type

# response = input("Would you like to have some food? (Y/N): ")

# if response == "Y":
#     print("Have some food")
# elif response == "N":
#     print("No food for you")
# else:
#     print("Why are you trying to prove yourself that you're a moron")


# # Boolean variables with if

# for_sale = False
# if for_sale:
#     print("Yes this item is for sale")
# else:
#     print("No this item is not for sale.")

# online = False
# if online:
#     print("The user is online.")
# else:
#     print("The user is offline")


# # One thing about if
# print("USING IF ON ALL CONDITIONS")
# num = 5
# # Using if only on all conditions and not elif
# if num>2: 
#     print("The number is greater than 2.")
# if num>3:
#     print("The number is greater than 3.")

# print()

# # Using if and elif 
# print("USING IF AND ELIF ON ALL CONDITIONS")

# if num>2: 
#     print("The number is greater than 2.")
# elif num>3:
#     print("The number is greater than 3.")



# # GRADE OF STUDENTS ON THE BASIS OF MARKS
# percentage = float(input("Enter the percentage of the student: "))
# if (percentage>=90):
#     print("The student has got an A grade")
# elif (80<=percentage<90):
#     print("The student has got a B grade")
# elif (70<=percentage<80):
#     print("The student has got a C grade")
# elif (0<=percentage<70):
#     print("The student must work harder.")
# elif (percentage<0):
#     print("Seriously dude. 😑😑😑😑😑😑")
# else:
#     print("What kind of grade do u have 🤔🤔🤔🤔🤔")

age = 80

if (age>=18):
    if (age>=80):
        print("The person is considered too old to drive.")
    else:
        print("The person can drive.")
else:
    print("The person is not eligible to drive.")