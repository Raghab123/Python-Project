# Typecasting = the process of converting a variable from one data type to another data type.
#               str(), int(), float(), bool()

name = "Bro Code"
age = 25
gpa = 3.17
is_student = True

type(name)  # Not printing. So no output displayed
print(type(name))  #Helps to identify the type of variable in the output. Here <class 'str'> states that
# it is a string variable. Similarly
print(type(gpa))  # Here gpa is a float variable because it has decimal place too. Because we inputted it so. (3.17)
print(type(is_student))  # is_student is a Boolean because we inputted it as True

gpa = int(gpa)  #Here it converted 3.17 into an integer removing the decimals by using int()
print(gpa)  # Pretty weird right. gpa is taking the nearest gpa input . gpa = int(gpa)

age = float(age)
age += 1  # Same as age = age + 1. We can do this addition and get 26 because it is a number and not a string.
print(type(age))  # We converted age into float first so it is showing as <class 'float'>
print(age)  # We got float i.e. decimal by using float() and got 25.0 + 1 = 26.0

str_age = str(age)  # We converted the age number into string. Basically its same as age = "25" instead of age = 25.
#String doesn't follow addition like numbers do. For eg: age = age + 1 would give me 26 if it were a number and not a
# string but if it were a string then, age = age + 1 is invalid. Instead, age = age + "1" is the correct input but the
# output will be different. i.e. 251. It just adds in character but not as an increase in number
print(str_age)  #This is due to the above conversion of age in float
print(type(str_age))  #Now it is shown as string because we converted it so

age = int(float(str_age))  #Converting string float number into integer. We have to compulsorily include float to convert
# it into integer. Integer doesn't round up. For rounding up we use round()
print(age)

#Whole number string. We don't need to use float to convert string number into integer because it isn't in float mode
age_str = "123"
age = int(age_str)  # Directly converts to integer 123
print(age)

#Decimal Number String. We need to compulsorily convert it into float because float is present here.
age_str = "123.45"
age = int(float(age_str))  # Converts to float 123.45, then to integer 123
print(age)

# INTERESTING WITH BOOLEAN. HERE IT CAN BE USED TO PROMPT A USER TO ENTER THEIR INFORMATION AGAIN IF THEY DON'T

name = bool(name)
print(name)

#If name = "" (nothing inside) then it will be false. We have to insert something the name even if it is a space bar. If
# it is nothing then it will so as false. IDK why

name = ""
name = bool(name)
print(name)

round(gpa)
print(gpa)
