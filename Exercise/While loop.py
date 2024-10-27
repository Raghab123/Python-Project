# # # # Print numbers from 1 to 100

# # # i = 1
# # # while i<100:
# # #     print(i,end=",")
# # #     i += 1

# # # if i == 100:
# # #     print(i)

# # # print("Loop ended")

# # # # Print numbers from 100 to 1

# # # i = 100
# # # while i>1:
# # #     print(i , end = ",")
# # #     i -= 1
# # #     if i == 1:
# # #         print(i)

# # # # Print the multiplication table of "n"

# # # n = float(input("Enter the number whose table of multiplication that you need: "))
# # # print(f"The table of multiplication of {n} is shown below: ")
# # # i = 1 
# # # while i <= 10:
# # #     print(f"{n} X {i} = {n*i}")
# # #     i += 1


# # # print()

# # # # Print the elements of the following list using a loop:

# # # my_list = [1,4,9,16,25,36,49,64,81,100]

# # # # Traverse == travelling over element in programming

# # # i = 0


# # # while i < (len(my_list)):
# # #     print(my_list[i])
# # #     i += 1

# # # print(end = "\n")

# # # for l in my_list:
# # #     print(l)


# # # Search for a number x in this tuple using loop:

# # new_list = [1, 4 , 9, 16, 25, 36, 49, 64, 81, 100, 36, 400, 100, 4556, 45, 30, 36]
# # mylist = tuple(new_list)
# # print(mylist)
# # x = int(input("Enter the number that you want to find: "))

# # idx = 0

# # while idx < len(mylist):
# #     if mylist[idx] == x :
# #         print(f"The number is found at index {idx + 1} starting from 1")
# #         idx +=1
# #     else: 
# #         print("finding...")
# #         idx += 1 

# # if idx == len(mylist):
# #     print(f'The number {x} is not found on the tuple after this')


# # # mylist = (1,1,2,3,4,4,5,6,7,7,8)
# # # # Maximum repeated numbers.
# # # # How many times
# # # # Positions of repetition
# # # # Least repeated and their position. How many times

# # # for i in range (0 , len(mylist)):
# # #     for j in range (1 , len(mylist)):
# # #         while j <= len(mylist):
# # #             if mylist[i] == mylist[j]:
                


# # # # tuple = (1,2,1,3,3,4,3,2,1,5,0,4,5,9) 




# # WAP TO FIND THE SUM OF FIRST N NUMBERS. (USING WHILE)


# while True:
#     while True:
#         try:
#             start = int(input("Enter the number that you want to start finding the sum from : "))
#             break
#         except:
#             print("This code only supports integer numbers. Not alphabets, symbols, decimal etc.")
    
#     again = input(f"You've entered {start} as the starting value of sum. Do you want to change it. N for no and Y for yes : ")

#     if again.upper() == "N":
#         break


# while True:
#     while True:
#         try:
#             stop = int(input(f"Enter the number that where you want to stop or the number upto which you want to find the sum starting from {start} : "))
#             break
#         except:
#             print(f"This code only supports integer numbers. Not alphabets, symbols, decimal etc.")
        
#     again = input(f"You've entered {stop} as the ending value of sum. Do you want to change it. N for no and Y for yes : ")

#     if again.upper() == "N":
#         break

# i = 1

# while i < (stop - start + 1):
#     next_number = start + i
#     if i == 1:
#         sum = start + next_number # Sum ma first 2 numbers ko sum store gareko hai. i == 1 huda. 1st iteration
#     else:
#         sum = sum + next_number
#     i += 1



# print(f"The sum of the numbers from {start} to {stop} is {sum}")

n = int(input("Enter the number upto which you want to find the sum of natural numbers : "))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(f"total sum : {sum}")
    

# WAP TO FIND THE FACTORIAL OF FIRST N NUMBERS. (USING FOR)

x = int(input("Enter the number that you want to find the factorial from : "))

