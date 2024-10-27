# Exercise 2. Shopping cart program

item = input("What item would you like to buy?: ")
price = float(input("What is the price of the item?: Rs "))
quantity = int(input("How many would you like? ")) # Quantity are whole numbers
total = price * quantity

print(f"You have bought {quantity} {item}")
print(f"Your total amount is Rs.{total} without tax.")