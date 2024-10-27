# Strings are immutable
str = "hello"
print(str[0]) # Letters and no. can be accessed but cannot be changed
# str[0] = "y" # Letters and no. cannot be changed partially
str = "yello"
print(str[0])

 # len = Length of the string. Including the spaces

str = "apple"
print(str[-3:-1]) # Negative slicing. Accessing from the end. Not negative index. Negative index doesn't exist. 
print(str.endswith("le"))


name = input("Enter your name: ")
print(len(name))
print(name[0]) # Accessing the zero position of string using indexing
print(name[0:len(name)]) # Slicing = Accessing parts of string

find = name.find("q") # .find gives the first occurrence of the given character. Starts from zero.
# Enter R and see for yourself. -1 output for the letters that aren't present there.
print(find)

# .rfind gives the last occurrence of the letter. Starts from zero again. Here "a" is 8 because space is included as well. The counting is done from left to right.
rfind = name.rfind("a")
print(rfind)

# .capitalize- capitalizes the first letter. .upper- capitalizes all the letters.  .lower - makes all characters lowercase

name = name.capitalize()
print(name)
name = name.upper()
print(name)
name = name.lower()
print(name)

# .isdigit returns as true or false. true if all characters are numbers only else false
# .isalpha returns as true or false. true if all characters are alphabets only else false. False even if space is present.

isdigit = name.isdigit()
print(isdigit)
isalpha = name.isalpha()
print(isalpha)


# .count - counts the number of particular character present in the string.
# .replace - replaces all the particular character with something that we input in the string.

phone_number = input("Enter your phone number: ")
count = phone_number.count("-")
print (count)

replace = phone_number.replace("-", "") # variable.replace("(old character)" , "(new character)")
print(replace)

# \n means next line
str1= "My name is Raghab Basnet.\nWe are creating it in python."
print(str1)

# print(help(str)) (Very messy )
