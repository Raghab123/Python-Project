# Functions is used to avoid redundancy. Not using this is a sign of bad programmer. Important in interview too.


# We can make functions that doesn't take any parameter and doesn't return any value

# def -- defining function

# def function_name(parameter1, parameter2, ...)=== This is called as function definition


def calc_sum(a,b):  
    # Inside parenthesis parameters can be entered i.e. input
    sum = a + b
    print(sum)
    return sum


print("BY USING FUNCTIONS")
calc_sum(5,10) # We are calling the defined functions

# function_name(argument1, argument2, ...) # function call . Argument supply value to the parameters

print("WITHOUT USING FUNCTION")
# No need of this
a = 5
b = 10
print(a+b)

calc_sum(12,7) # We don't need to print this because it is already printed in the definition

print("Print not defined inside the function")

def new_calc_sum(a,b):
    return a + b

print(new_calc_sum(1,2))

def hello():
    for i in range(0,5):
        print("HELLO FROM THE OTHER SIDE")

hello() # Parenthesis is important

print(hello()) # No return here so none


# Average of 3 numbers:

def calc_avg(a,b,c):
    avg = (a+b+c)/3
    print(avg)
    return avg

calc_avg (2,3,4)


print("apnacollege","raghab basnet") # Print is a built in function and apnacollege is an argument that is stored inside the definition of print function 
# sep = " "


print("apnacollege")
print("raghab") # end = "\n"

print("apnacollege" , end = "$")
print("raghab") 


# len()
# range()

# User defined functions


# Default parameters. Used when no value is given to an argument

def cal_prod(a=2, b=3):
    print(a*b)
    return a*b

print("When no argument is given. Using default parameters")
cal_prod() # No value is given to the argument

print("When argument is given")
cal_prod(4,5)

def cal_prod(a,b=2): # Parameter without a default is followed by parameter with a default. Meaning the last parameter must always have a default value if the one before it is doesn't have a value.

# def cal_prod(a = 2, b) Not possible
    print(a*b)
    return a*b

cal_prod(4)