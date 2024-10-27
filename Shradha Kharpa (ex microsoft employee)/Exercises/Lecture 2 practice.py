# # #  WAP TO INPUT USER'S NAME AND PRINT THE FIRST NAME

# name = input("Enter your name: ")
# find = name.find(" ")
# if find == -1:
#      print(name)
# else:
#     print(f"Your first name is {name[0:find]}")

# print(f"The length of the name is {len(name)}")

# # # WAP TO INPUT THE USER'S LAST NAME AND PRINT THE LAST NAME

# name = input ("Enter your full name: ")
# rfind = name.rfind(" ")

# while rfind == -1:
#     print(f"{name} is not your full name.")
#     name = input ("Enter your full name: ")
#     rfind = name.rfind(" ")

# last_name = name[rfind+1:]
# print(f"Your last name is {last_name}")


# PROBLEM HERE !!!!!!
name = input('Enter your full name: ')
rfind = name.rfind(" ")

while True: 
    if rfind != -1:
        print(f"Your last name is {name[rfind+1:]}")
        break
    else:
        print("Please enter your full name.")
        name = input('Enter your full name: ')
        rfind = name.rfind(" ")

last_name = name[rfind+1:]

print(last_name)
        
        
# # To find the occurrence of $ in the string
# str = input("Enter anything you like: ")
# dollar = str.count("$")
# print(f"In the input that you have given there are a total of {dollar} occurrences of $ sign")


# import time
# #  WAP TO CHECK IF A NUMBER ENTERED BY THE USER IS ODD OR EVEN
# print("The code here is about to check whether a number is odd or even.")
# time.sleep(1)
# num = int(input("Enter a number: "))
# if (num%2==0):
#     number = "even"
# else:
#     number = "odd"

# print(f"The number s{num} is {number}")


# WAP TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY THE USER

# import math

# print("Here the code is entered in such a way to find the greatest of three numbers")

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# # max = max(num1,num2,num3)

# # print(f"The greatest of the three numbers is {max}")

# if num1<num3 and num3>num2:
#     num = num3
# elif num1<num2:
#     num = num2
# else:
#     num = num1
# print(f"The greatest number is {num}")

import time
# WAP TO CHECK IF A NUMBER IS A MULTIPLE OF 7 OR NOT

print("WAP TO CHECK IF A NUMBER IS A MULTIPLE OF 7 OR NOT")

time.sleep(1.5)

print("You ready?")

time.sleep(1.5)

print("Here we go.", end=" ")

num = int(input("Enter a number: "))

if num%7==0:
    print(f"{num} is a multiple of 7")
else:
    print(f"{num} is not a multiple of 7")