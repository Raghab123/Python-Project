# Python calculator

operator = input("Enter an operator (+ - * /): ")


if operator == "+" :
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = num1+num2
    print(f"The round up result will be {round(result, 3)}")
elif operator == "-" :
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = num1-num2
    print(f"The round up result will be {round(result, 3)}")
elif operator == "*" :
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = num1*num2
    print(f"The round up result will be {round(result, 3)}")
elif operator == "/" :
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result = num1/num2
    print(f"The round up result will be {round(result, 3)}")
else:
    print(f"{operator} is not a valid operator")

