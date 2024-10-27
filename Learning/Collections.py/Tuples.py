# Tuple = () ordered and unchangeable. Duplicates Ok. Faster than lists. Use tuples over lists if u can. No assignment like fruits[0] = "banana"



tup = (1) # Python perceives this as an integer
print(type(tup))
tup = ("hello") # Python perceives this as a string
print(type(tup))
tup = (1,) # Python now takes this as a tuple
print(type(tup))
tup = ("hello",) # Python now takes this as a tuple
print(type(tup))

# This comma is necessary when we have a single value in the tuple. Check with print(type(tup))

 
fruits = ("apple","banana","orange","coconut","coconut")

for fruit in fruits:
    print(fruit) # fruit not necessary just variable like x. Just for the sake of proper english

# print(dir(fruits)) # Guide to what we can do with the current scope 
# print(help(fruits))

print(len(fruits)) # Total variables inside here.

print("pineapple" in fruits)

print(fruits.index("apple"))

print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit)