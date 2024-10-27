#Variable= A container for a value (string, integer, float, boolean)
#          A variable behaves as if it was the value it contains
# A variable must be simple, short and meaningful
# Comment shortcut = CTRL/CMD + /

# All the things inside the double quotation are strings. They can be anything. Numbers, alphabets.
first_name = "Raghab" # "=" is the assignment operator

print(first_name) # Don't use double quote here to print the first name or else it will literally print first_name and
#not Raghab. Without double quote or any other quote like single quotation too. it will print Raghab.

print(f"Hello {first_name}") #first_name here  is "Raghab" f stands for format. Adding something to our string "first-
#-name I guess. Here Hello is added

print(f".See you on the other side.{first_name}")

email = "Bro123@fake.com"
print(f"Your email is {email}")

#Integers= Cannot be inside quotes otherwise it will be a string technically 😊.
age = 25
quantity = 3
number_of_students = 30 # We cannot write number of students. They have to be connected by something
temperature = -40

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"You class has {number_of_students} students")
print(f"The temperature is around {temperature}℉ ")

# Float (It includes decimal too)
price = 10.99
gpa = 3.17
distance = 5.3 # no kilometer or anything in integers or float
temperature = -273.15

print(f"The price is Rs {price}")
print(f"My GPA is {gpa}")
print(f"You ran {distance}km")
print(f"The temperature is {temperature}℃")

#Boolean= True or False. Isn't generally used in the output of the program like below but more with if statements inside a program
# The Boolean must have 1st character of True and False capital else python won't understand it as a boolean as python is case sensitive

is_student = False
print (f"Are you a student?: {is_student}")

if is_student:
    print("So you are a student")
else:
    print("So you are not a student")

for_sale = False

if for_sale:
    print("This item is for sale")
else:
    print("That item is not for sale")

is_online = True

if is_online: # colon must be present
    print("You're online")
else:
    print("You're offline")

# None -- Where no value can be stored
a = None
old = False
print(type(a))
print(type(old))