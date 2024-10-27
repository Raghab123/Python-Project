# # # # WAP TO ASK THE USER TO ENTER THE NAME OF THEIR 3 FAVORITE MOVIES AND STORE THEM IN A LIST

# # fav_movies = []

# # fav_movies.append(input("Enter the 1st movie that you like: "))
# # fav_movies.append(input("Enter the 1st movie that you like: "))
# # fav_movies.append(input("Enter the 1st movie that you like: "))
# # print(f"The movies that you like are {fav_movies}")

# # # Co Pilot idea
# # fav_movies = []

# # for i in range(1, 4):
# #     movie = input(f"Enter the {i}st/nd/rd movie that you like: ")
# #     fav_movies.append(movie)

# # print(f"The movies that you like are {fav_movies}")

# # fav_movies.clear()
# # print(fav_movies)


# # for i in range(1,4):
# #     if i == 1:
# #         suffix = "st"
# #     if i == 2:
# #         suffix = "nd"
# #     if i == 3:
# #         suffix = "rd"
# #     movie = input(f"Enter the {i}{suffix} that you like: ")
# #     fav_movies.append(movie)

# # print(f"The movies that you like are {fav_movies}")

# WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS

list = []

items = input("Enter the items that you want for the list: ")

list = [item.strip(", ") for item in items.split()]
print(list)

reverse_list = list.copy()

reverse_list.reverse()
print(reverse_list)

if list == reverse_list:
    p = "a palindrome"

else:
    p = "not a palindrome"

print(f"The list is {p}")


# # list.clear()

# # for item in items.split():
# #     add = item.strip(", ")
# #     list.append(add)  
# # print(list)

# # list.clear()
# # for item in items.split():
# #     list.append(item.strip(", "))
# #     print(list) # Prints for each iteration. Just understanding why print(list isn't inside consider inside the loop)


# # WAP TO COUNT THE NUMBER OF STUDENTS WITH THE "A" GRADE IN THE FOLLOWING TUPLE

# tup = ("C","D","A","A","B","B","A")
# print(f"The number of students with grade A is {tup.count("A")}")
# print("The no. of students with grade A is " + str(tup.count("A")))



# # STORE THE ABOVE VALUES IN A LIST AND SORT THEM FROM "A" TO "D"


# list = ["C","D","A","A","B","B","A"]
# list.sort()
# print(list)

# # STORE THE FOLLOWING WORDS MEANINGS IN A PYTHON DICTIONARY:
# # table: "a piece of furniture","list of facts and figures"
# # cat : "a small animal"


# dict = {
#     "table" : ["a piece of furniture","list of facts and figures"],
#     "cat": "a small animal"
# }

# print(dict)

# # You are given a list of subjects for students. Assume one classroom is required for 1
# # subject. How many classrooms are needed by all students.
# # ”python”# “java”# “C++”# “python”# “javascript”# “java”# “python”# “java”# “C++”# “C”


# list = {"python","java","C++","python","javascript","java","C++","C"}

# no_of_class = len(list)

# print(f"The no. of classroom required by the students is {no_of_class}") 



# # WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value

# # sub1 = []
# # sub2 = []
# # sub3 = []


# # for i in range(1,4):
# #     if i == 1:
# #         suffix = "st"
# #         name1 = input(f"Enter the name of the {i}{suffix} subject: ")
# #         update = float(input(f"Enter the marks of {name1}: "))
# #         sub1.append(update)
        

# #     if i == 2:
# #         suffix = "nd"
# #         name2 = input(f"Enter the name of the {i}{suffix} subject: ")
# #         update = float(input(f"Enter the marks of {name2}: "))
# #         sub2.append(update)

        
# #     if i == 3:
# #         suffix == "rd"
# #         name3 = input(f"Enter the name of the {i}{suffix} subject: ")
# #         update = float(input(f"Enter the marks of {name3}: "))
# #         sub3.append(update)


# # subject = {
# #     f"{name1}" : sub1,
# #     f"{name2}" : sub2,
# #     f"{name3}" : sub3
# # }

# # print(subject)


# # Sharadha's idea
# subject = {}

# x = input("Enter the marks in physics: ")
# subject.update({"phy": x})

# x = input("Enter the marks in chemistry: ")
# subject.update({"chemistry": x})

# x = input("Enter the marks in maths: ")
# subject.update({"maths": x})

# print(subject)


# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

my_list = ["9","9.0"]
print(set(my_list))

nine = {
    ("float",9.0),
    ("integer",9)
}
print(nine)