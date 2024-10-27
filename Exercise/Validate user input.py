# Validate user input
# 1. User input cannot be more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits
# Looping until the correct input

while True:
    user_name = input("Enter your username: ")

    # Check if the username is more than 12 characters
    if len(user_name) > 12:
        print("Your username isn't valid: Username cannot be more than 12 characters long.")
        continue  # Ask for input again

    # Check if the username contains spaces
    if ' ' in user_name:
        print("Your username isn't valid: Username must not contain spaces.")
        continue  # Ask for input again

    # Check if the username contains digits
    if not user_name.isalpha():
        print("Your username isn't valid: Username must not contain digits.")
        continue  # Ask for input again

    # If all conditions are satisfied
    print(f"Welcome {user_name}")
    break  # Exit the loop
