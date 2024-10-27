# collection = single "variable" used to store multiple values of different data types together in the same collection variable but not in arrays of C++ where similar type of data need to be stored in a collection
# Lists and tuples are mutable but strings and sets are not mutable

student = ["Raghab" , 19 , "boy"]

# Lists = [] ordered and changeable. Duplicates are OK

fruit = "apple"
print(fruit)
print()

# Lists
print("Lists")
fruits = ["apple","orange","banana","coconut"]
print()
print(fruits)

print()
print("Accessing the variables of an index")
print()
print(fruits[1]) # Access values within the list by using the index operator. If no values are outside the range of numbers then index error appears

print(fruits[:3])
print(fruits[::2])
print(fruits[::-1])
print(fruits[2:5])
print(fruits[-3:-1])


print("For loop")
for fruit in fruits:
    print(fruit) # fruit not necessary just variable like x. Just for the sake of proper english

# print(dir(fruits)) # Guide to what we can do with the current scope 
# print(help(fruits))

print('Total no. of items in the list :', end=" ")
print(len(fruits)) # Total variables inside the list here.
print()

print("Using in operator to find variable in a list")
print()
print("pineapple" in fruits)
# "in" is an operator without double quotation. Returns as boolean. It is used to find a value within a list

print("Assigning pineapple as the first variable in the list. A little different from sets. I")
fruits[0] = "pineapple" # This deletes the first variable and takes it space
print()
for fruit in fruits:
    print(fruit)
print()


print("Appending, removing, inserting, reversing etc.")
print()

print("1.",end=" ")
fruits.append("mango") # Add an element at the end of the list
print(fruits)

print("2.", end=" ")
fruits = ['pineapple','pineapple', 'orange', 'banana', 'coconut', 'mango']
fruits.remove("pineapple")# Remove only the first occurrence of an element
print(fruits)

print("3." , end = " ")
fruits.insert(0,"apple") # This doesn't delete like fruits[0]="pineapple" but just adds on the list pushing the 1st name of the list and taking its place
print(fruits)

print("4.", end = " ")
fruits.reverse() # Reversed on the basis of our input. Not alphabetically
print(fruits)

print("5.", end = " ")
fruits.sort()
print(fruits)

print("6." , end = " ")
fruits.sort(reverse = True) 
print(fruits)

print("7." , end = " ")
print(fruits.index("apple")) # To find the position

print("8." , end = " ")
print(fruits.count("banana")) # Number of bananas present in the list. For duplicates detection

# fruits.clear("banana")
# print(fruits). This doesn't work in python. clear() takes no arguments.

print("9." , end = " ")
fruits.clear() # Remove everything
print(fruits)

fruits = ['pineapple', 'orange', 'banana', 'coconut', 'mango']
print(fruits.pop(4)) # Takes index value. Not like remove that takes variables.
print(fruits) 