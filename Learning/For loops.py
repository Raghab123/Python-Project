# # for loops = execute a block of code for sequential traversal (travelling in a sequence) over datatypes like lists, tuples etc
# # You can iterate over a range, string, sequence, etc.

# # Syntax

# # for el in list
# #     some work

# # else: ( Not compulsary but used in break hai when we don't want further execution)
# #     work when loop ends

# import time 

# for i in reversed(range(1, 11, 1)): # The second number is exclusive
#     print(i) # The code should be indented here.
#     time.sleep(1)
# print("Happy New Year!")
# print()



# for i in range (1,11,2):
#     print(i)
#     if i >= 1:
#         time.sleep(2)

# print("Happy New Year")

# time.sleep(1)

# '''Credit card number'''
# credit_card = "1234-5678-9012-3456"
# for x in credit_card:
#     print(x, end="")
# print()    
# print()

# # Not printing 13 from numbers 1 - 20
# for x in range(1,21):
#     if x==13:
#         continue # Continue just skips the part and keeps the loop going. Break shuts down the following loop too
#     elif x<19:
#         print(x,end=",")
#     if x == 19:
#         print(x)
# print()
# print()


# for x in range (1,21):
#         if x < 12:
#             print(x,end=",")
#         elif x == 12:
#             print(x)
#         else:
#             break
            
            
    

# print()

# for x in range(1,21):
#     if x<1:
#         print(x,end=",")
#     else:
#         break



# print(3 * 2 * "-")



# credit_card = "1234-5678-9012-3456"
# for index, x in enumerate(credit_card):
#     print(f"Index: {index}, Character: {x}")

# With else
str = "apnacollege"

for char in str:
    if char == 'o':
        print('o found')
        break
    print(char)

else:
    print("End")

print()

# Without else

str = "apnacollege"

for char in str:
    if char == 'o':
        print('o found')
        break
    print(char)


print("End")