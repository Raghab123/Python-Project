# f = f + 1 is same as f += 1
# f -= 2 is same as f = f - 2
# f = f * 5 is same as f *= 5
# f = f / 2 is same as f /= 2
# f = f ** 2 is same as f **= 2. Exponent
# % is MOD that gives us the remainder. This can be used to find whether a number is even or odd. Number % 2. If answer
# is 0 then even else odd
# round() - to round up
# abs() - absolute value- the distance away from 0.
# pow(base, exponent) - power function
# max(x,y,z)- maximum value and similarly min (x,y,z)

# Relational Operators
# Its output is a Boolean
# == --- for equality not assignment
# != --- not equal to operator
# < --- less than operator
# > --- greater than operator
# >= --- greater than or equal to 
# <= --- less than or equal to 
# ! generally means no here

a = 50
b = 20
print(a == b) # False
print(a != b) # True

f = 5
f = f ** 2
print (f)
remainder = f % 3
print(remainder)
f = 6
remainder = f % 3
print(remainder)
x = -3.14
print(round(x))
print(abs(x))
print(pow(4,3))
print(max (3,5,-1))
print(min(4,-5,0))

