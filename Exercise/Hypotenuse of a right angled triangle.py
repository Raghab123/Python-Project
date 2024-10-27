import math

p = input("Enter the length of perpendicular of a right angled triangle: ")
b = input("Enter the base of perpendicular of a right angled triangle: ")
a = float(p) ** 2
b = float(b) ** 2
print(f"The hypotenuse of the given right angled triangle is {math.sqrt(a+b)}")

# Faster method
p = float(input("Enter the length of perpendicular: "))
b = float(input("Enter the length of the base: "))
print(f"The length of hypotenuse of the right angled triangle is {math.sqrt(pow(p,2) + pow(b,2))}")