import math

# Always a safe approach to use float mostly in case of maths problem to avoid any problems or hassle

pi = math.pi
while True:
    r = float(input("Enter the radius of the circle: "))
    if r >= 0:
        break
    else:
        print("Radius cannot be negative. Please enter a positive value.")
C = 2 * pi * r
print(f"The circumference of a circle with radius {r} units is found out to be {C} units")
C = round(C)
print(f"If this value is rounded up then it is nearly equal to {round(C)} units")