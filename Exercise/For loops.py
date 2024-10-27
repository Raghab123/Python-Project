

# # # Print the elements of the following list using a loop:

# # mylist = [1,4,9,16,25,36,49,64,81,100]

# # print(len(mylist))

# # i = 1
# # for list in mylist:
# #     if i < len(mylist):
# #         print(list, end = ",")
# #         i += 1
# #     else:
# #         print(list)

# # Search for a number x in this tuple using for loop 

# mylist = [1,4,9,16,25,36,49,64,81,100,64,4]

# # Here we are doing a linear search. Imp

# import time

# mylist = tuple(mylist)

# x = int(input("Enter the number that you want to search in the tuple : ")) 
# # I mistakenly removed int from here
# i = 1
# not_found = True

# for find in mylist:
#     if find == x :
#         print(f"The number is found in the position {i} starting from 1 as first ")
#         not_found = False
#     else:
#         print("finding " , end = " " , flush = True )
#         for j in range (1,4):
#             # time.sleep(0.25)
#             print("*" , end = " " , flush = True)
#         time.sleep(0.2)
#         print() # Mess with this print inside and outside of the loop. It has to do with it being a part of the iteration where the weirdness comes.
#     i += 1
        
# if not_found :
#     print(f"The number {x} cannot be found in the given tuple. ")
#     time.sleep(0.25)
#     print("End of search result.")

# else: 
#     print("End of search result.")



# # WAP TO FIND THE FACTORIAL OF FIRST N NUMBERS. (USING FOR)

# n = int(input("Enter the number to find its factorial : "))

# factorial = 1 # Initialized by 1. Because if variable is multipled by 0 then answer is always zero.

# for i in range(n, 0, -1):
    
#     factorial *= i
    
# print(f"The factorial of {n} is {factorial}")

n = 4

factorial = 1

while n >= 1:
    factorial *= n
    n -= 1
print(factorial)