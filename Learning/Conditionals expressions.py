# Conditional expressions = A one-line shortcut for if-else statement (ternary operator)
#                            Print or assign one of two values based on a condition
#                           X if condition else Y

a = input("Enter the number: ")
a = float(a)
result = "Even" if a % 2 ==0 else "Odd"
print(f"The given number i.e. {a} is {result}")


# maximum number
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

max_num = a if a>b else b
min_num = a if a<b else b

print(f"The maximum number is {max_num} and the minimum number is {min_num}")

# Age status

age = int(input("Enter the age: "))
status = "Child" if 0<= age < 18 else "Adult"
print(status)

# Weather

temp = float(input("Enter the temperature: "))
status = "Hot" if temp > 20 else "Cold"
print(status)

# User role

user_role = input("Enter your role: ")
status = "Full Access" if user_role == "admin" else "Limited Access"
print(status)