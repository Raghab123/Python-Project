# Shopping cart program
# related to collections.py

foods = [] 
prices = []

# The lists foods and prices are initialized as empty lists, which means they are ready to have items appended to them


while True:
    food = input("Enter the food that you want (q to quit): ")
    if food.lower() == "q":
        print("Thank you for your time")
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)
print("-----YOUR CART-----")

for food in foods:
    print(food, end = ",")
