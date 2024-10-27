# format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 34523.14159
price2 = -98703.65
price3 = 12754.34

# Rounding to specific decimal places
print("Rounding to specific decimal places")
print(f"Price 1 is ${price1:.1f}")
'''Here f means floating point number. 1f meaning 1 decimal place and so on. '''
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.3f}")

print(end="\n")


print("Allocating spaces")
# Allocating Spaces
# Allocating spaces ensures that a string or number is displayed with a specific total width, filling in with spaces if necessary.
# This is useful for aligning text or numbers in columns.

# Syntax
# print(f"{value:width}")
# - width specifies the total width of the output, including the number or string itself and any padding.

print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:20}")
print(f"Price 3 is ${price3:30}")

print(end="\n")

# Zero padding. Zero padding only adds zeros if the total width specified is greater than the length of the string.
# If the length of the string is equal to or greater than the specified width, no zeros will be added.

print("Zero padding")
print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:020}")
print(f"Price 3 is ${price3:030}")

print(end="\n")

# :+ = use a plus sign to indicate positive value or in general := means place sign to leftmost position

print("Use of + sign")
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

print(end="\n")
print("Use of space ")
# :  = insert a space before positive numbers only. Not in negative numbers
print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")

print(end="\n")


print("Use of comma separator")
# :, = comma separator. It also does the work of showing -ve sign hai.
print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")

print(end="\n")


print("Use of all the combination above")
# Combination of all the above
print(f"Price 1 is ${price1:-,.2f}")
print(f"Price 2 is ${price2:-,.2f}")
print(f"Price 3 is ${price3:-,.2f}")

print(end="\n")

"""In the context of Python’s string formatting, the + and - signs are used to control the display of the signs for both positive and negative numbers, rather than performing any mathematical operations"""

# Arrangements
print("Arrangements")

text = "Hello"
print(f"{text:<10}")  # Output: "Hello     "
# Here, < specifies left alignment
print(f"{text:>10}")  # Output: "     Hello"
# Here, > specifies right alignment
print(f"{text:^10}")  # Output: "  Hello   "
# Here, ^ specifies left alignment

# Arrangements with padding
print("Arrangements with padding")
print(f"{text:-<10}")  # Output: "Hello-----"
# Here, -< specifies left alignment with padding character '-'

print(f"{text:*>10}")  # Output: "*****Hello"
# Here, *> specifies right alignment with padding character '*'

print(f"{text:.^10}")  # Output: "..Hello..."
# Here, .^ specifies center alignment with padding character '.'

print("Raghab is my name.","My age is 19.")
print(23+7)

print(f"{text:/^11}")