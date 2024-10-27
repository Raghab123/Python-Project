# logical operators = evaluate multiple conditions
#                or = at least one condition must be true
#               and = all conditions must be true
#               not = inverts the condition (True --> False and False --> True)

# OR
temp = -5
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")

else :
    print("The outdoor event is still scheduled")

# AND
if 0<temp<25 and is_raining :
    print("It's a cold and rainy day. Stay warm!")
elif temp<=0 and is_raining:
    print("Are you guys getting ice for free and is the rain being converted into ice?")
else:
    print("The weather must be pleasant there right")

# NOT. Here its basically trying to make the condition true for the sake of AND operator to work. We need to modify the
# comments accordingly just to make sense.

temp = 35
is_raining = True

if 0 < temp < 25 and not is_raining:
    print("It's a cool day, and it's not raining.")
elif temp <= 0 and not is_raining:
    print("It's freezing outside, but at least it's not raining.")
elif is_raining and temp<=0:
    print("It's raining. Don't forget your umbrella! Also its very cold. Wear warm clothes")
elif temp>=35 :
    print("The weather is very hot")
else:
    print("The weather must be pleasant there, right?")



