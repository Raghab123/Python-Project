import math

while True:
    r = float(input("Enter the radius of the circle: "))
    if r >= 0 :
        break
    else:
        print("Radius cannot be negative. Please enter a positive value")

A = math.pi * pow(r,2) # Alternatively A = math.pi * r ** 2
print(f"The area of the circle having radius {r} units is {A} square units which when rounded up gives {round(A)}")

if A == 0:  # comparing so ==. 
    print ("It is a point circle.")