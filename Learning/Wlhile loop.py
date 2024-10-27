# # while loop = execute some code WHILE some condition remains true. BEWARE OF INFINITE LOOPS

# name = input("Enter your name: ")

# while name == "" or " ":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
    
#     '''This input is a must. If we don't have this input right after the while loop then an infinite loop of you did not enter your name will appear. So the input needs to be there so that once the user inputs their name the while loop will no longer be true. 
#     We will never reach the print statement part.'''

#     '''print(f"Welcome {name}")''' '''This is a problem. This is within the while loop so if I just hit enter it will 
#     ask me to enter my name again but it will also show me Welcome (blank). So the print has to be outside of while 
#     loop here. Else it becomes the part of that loop. Try by removing the triple thingy and see for yourself.'''

# print(f"Welcome {name}")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age cannot be less than zero")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old.")

# while True:
#     food = input("Enter the food you like (q to quit): ")

#     if food == "":
#         print("Please enter a food that you'd like or click q to quit")
#     elif food == "q":
#         print("Okay bye")
#         break
#     else:
#         print(f"You like {food}")
#         break # If I don't break this then it will keep asking me the food I like and I can't go to the other code.

# # This part will only execute after the first loop ends
# num = int(input("Enter a number between 1 and 10: "))

# while num < 1 or num > 10:
#     print(f"The number {num} is not valid.")
#     num = int(input("Enter a number between 1 and 10: "))

# print(f"Your number is {num}")


# message = "Hello my name is Raghab"
# print(message)

# message = "Hello my full name is Raghab Basnet"
# print(message)

# # Break = terminate the loop
# # Continue = terminates execution in the current iteration and continues execution of the loop with the next iteration

i = 0

while i <=5 :
    if i == 3 :
        i += 1
    print(i)
    i +=1 

i = 1
while i <=10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1