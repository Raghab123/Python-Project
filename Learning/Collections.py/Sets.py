# Sets = {} unordered and immutable (the values cannot be altered), but Add/Remove Ok. No duplicates allowed
# Sets are mutable but their elements are immutable.
# We can add or remove but we can't overwrite the elements
# According to bro code it works with constants
# Sets can store strings, int, float, boolean, tuples because their values cannot be altered but dictionaries are lists are mutable so they cannot be stored in sets

fruits = {"apple","banana","orange","coconut"}
print(fruits)

# Index operator has no significance here because the set is unordered.
# print(fruits[0])
# Error was shown so in comments

for fruit in fruits:
    print(fruit) # fruit not necessary just variable like x. Just for the sake of proper english

# print(dir(fruits)) # Guide to what we can do with the current scope 
# print(help(fruits))

print(len(fruits)) # Total variables inside the list here.

print("pineapple" in fruits)

fruits.add("pineapple") # added to a random position
print(fruits)

fruits.remove("apple")
print(fruits)

print(fruits.pop()) # Remove the first element of the output i.e. random output. The print here shows the element removed.
print(fruits)

fruits.clear() # I made a mistake here by not keeping the brackets
print(len(fruits))
print(fruits)

fruits = {"apple","banana","orange","coconut", "coconut"} 
print(len(fruits)) # despite 5 items present set consider it as 4 items. In all languages
print(fruits) # only one coconut is shown as the output


fruits = {} # Empty dictionary. Not an empty set
print(type(fruits))

fruits = set() # Empty set
print(type(fruits))
# fruits.add([1,2,3]) List creates an error here. Unhashable ---> dictionaries, lists, sets too.
 
fruits.add((1,2,2))
print(fruits)

# set1.union(set2) --> Combines both set values and returns a new value

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1)
print(set2)

# set1.intersection(set2) --> Combines common values and returns new 

print(set1.intersection(set2))