# Python weight calculator


weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (Kg or Lb): ")

if unit == "Kg" :
    weight = weight * 2.205
    unit = "Lb"
    print(f"Your weight is {round(weight,2)} {unit}")

elif unit =="Lb" :
    weight = weight / 2.205
    unit = "Kg"
    print(f"Your weight is {round(weight,2)} {unit}")

else:
    print("The unit is not valid")


