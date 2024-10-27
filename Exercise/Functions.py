# Wap to print the length of a list. (list is the parameter)

mylist = [1,2,3,4,5,"Raghab", "Garima", "Paribesh"]

heros = ["ironman", "captain america", "thor", "shaktiman"]

def length_list(list):
    print(len(list))
    

length_list(mylist)
length_list(heros)


# WAP TO PRINT THE ELEMENTS OF A LIST IN A SINGLE LINE. (LIST IS THE PARAMETER)

def elemenets_of_list(list):
    j = 1
    for i in list:
        if j < len(list):
            print(i, end = ",") # Last number vanda paila samma comma hoos vanera
        else:
            print(i)
        j += 1

elemenets_of_list(mylist)
elemenets_of_list(heros)


print()
print()
# % indicates trailing factor

# WAP TO FIND THE FACTORIAL OF N. (N IS THE PARAMETER)

import time

def factorial_n():

    while True:
        try:
            n = int(input("Enter the number to find the factorial of : "))
            break
        except:
            print("Please enter the number in figures only.")
            time.sleep(0.5)
        
    if n == 0:
        print("The factorial of {n} is 1.")

    elif n < 0:
        print("The factorial of {n} is not possible.")
    
    else:
        factorial = 1
        for i in reversed(range(1,n+1)):
            factorial *= i
        print(factorial)

factorial_n()

# WAP TO CONVERT USD TO NPR

def convert_n():
    print("This program converts USD into NPR and vice versa")
    while True:
        try:
            x = input("Enter the currency that you have the amount on. USD or NPR : ")
            break
        except:
            print("Please enter either USD or NPR only.")

    if x.upper() in ["USD" , "$"]:
        while True:
            try:
                n = float(input(f"Enter the amount in {x.upper()} : "))
                break
            except:
                print("Enter the digits only.")

        result = n * 135

        print(f"The amount for {x.upper()}{n} is NPR {result:,.2f}")


    elif x.upper() in ["NPR" , "RS"] :
        while True:
            try:
                n = float(input(f"Enter the amount in {x.upper()} : "))
                break
            except:
                print("Enter the digits only.")

        result = n / 135

        print(f"The amount for {x.upper()}{n} is USD {result:,.2f}")

        
convert_n()


# Indentation is very important. result ra last print skip vayeko thiyo break le garda

# WAP to find whether a number is even or odd

def find_even_odd():

    while True:
        try:
            n = int(input("Enter a number in terms of figure : "))
            break 
        except:
            print("The input doesn't support alphabets, symbols etc. Only integer")

    if n % 2 != 0:
        num = "Odd"

    else:
        num = "Even"

    print(f"The number {n} is {num}")

find_even_odd()