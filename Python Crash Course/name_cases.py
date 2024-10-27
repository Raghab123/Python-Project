name= "eric waller"
print("Hello " + name.title() + "," + " Would you like to learn some Python today?")
# No + sign after a comma. + sign adds two strings not a comma and a string. Make everything string. Like this 
# print("Hello " + name.title() + ", Would you like to learn some Python today?")


upper = print(name.upper()) # Upper makes all letter capital
lower = print(name.lower()) # Lower makes all letter small
title = print(name.title()) # Title makes all starting letter capital

name = "David Goggins"
message = '''"Don't stop when you're tired, stop when you're done."'''

print(name + " once said, " + message )

name = "   David   Goggins    "

print("\n" + name ) # \n creates a new line = newline
print("\t" + name ) # \t creates a tab or gap in the same line = tab
# Both tab and newline can be combined. Always inside a inverted comma. name is a variable not a string so it is not inside a inverted comma 

print(name.lstrip()) # Remove gap from the left side only
print(name.rstrip()) # Remove gap from the right side only
print(name.strip()) # Remove gap from both ends only