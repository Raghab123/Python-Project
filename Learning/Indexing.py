# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-7456-2763-4532"

print(credit_number[0]) # Python always starts from 0 like we start from 1
print(credit_number[0:4]) # The starting index is inclusive but the ending index is not inclusive. So it can be written as [:4]
print(credit_number[5:]) # The starting index i.e. from 1 of "1234-....32" starting as 0, 1, 2, and so on. 5 is 4 and [5:] means starting from the 5th index or the 6th character upto to the last character of the entire string. 0 = 1 , 1 = 2 hai. Careful hai.
# Negative index starts from the end of the character like -1 means the last character. Similarly -2 means the 2nd last character
print(credit_number[-1])
print(credit_number[-2])

# step
print(credit_number[::2]) # If the starting and the ending is not completely filled then python will assume everything included step = 2. That will print every two-step consecutive character
print(credit_number[::3])


# Write a program to get the last 4 digits of a credit card number
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# Reverse the credit card number. To reverse a string, set the string in -1
reverse = credit_number[::-1]
print(f"The reverse of the credit card is {reverse}")


# Padding before the last 4 digits of the credit with "X" and "-"" "XXXX-XXXX-XXXX-4532"

for x in range (1 , 16):
    if x % 5 == 0 :
        print("-" , end="")
    else: 
        print("X",end="")

print("4532")

