# # Store data in key:value pair like word:meaning.
# # Unordered, mutable, no duplicates (like a real life dictionary. One word can store multiple meanings but the same word will not be seen multiple times). Use {}
# # Key can be anything that doesn't change with time. Can even be a tuple

# info = {
#     "key" : "value",
#     "name" : "apnacollege",
#     "learning" : "coding",
#     "age" : 35,
#     "marks" : 3.17,
#     "subjects" : ["python", "C", "Java"],
#     "is_adult" : True,
#     12.99 : 94.4
# }

# print(info)
# print(type(info))

# print(info["name"])
# print(info["subjects"])
# print(info["age"])

# # Overwrite

# info["name"] = 23 
# info["surname"] = "Basnet"
# print(info)

# info = {

# }
# print(info)

# null_dict = {}

# null_dict = {
#     "age" : 20
# }
# print(null_dict)


# Nested Dictionaries

student = {
    "name":"Shova Basnet",
    "subjects" : {
        "Phy":73,
        "Chem":71,
        "Maths":75
    }  
}

# print(student["subjects"]["Chem"])

# # .keys() brings all the keys present but not the neested keys
# print(student.keys())

# print(len(student)) # Print the total no. of keys 

# print(list(student.keys()))
# print(len(list(student.keys())))



# # .values() = Gives all the values

# print(student.values())

# # .items() = returns all (key,value) pair as tuples

# print(student.items())
# pairs =list(student.items())
# print(pairs[0])


#.get(key) = returns key according to value


print(student["name"])
print(student.get("name"))

# print(student["name2"]) will show me an error but
# print(student.get["name2"]) will show me NONE instead of error.
# Error in the program will stop the execution and no further code can be executed but .get will just show None if error and the program will be further executed


# .update({newDict}) = inserts the specified items to the dictionary

add_dict = {"city": "delhi","movie":"Shutter Island","name":"Raghab Basnet"} # I made an error here by creating two separate dictionaries with four curly brackets. Two for city and delhi and the rest for movie and shutter island. Also the updated key:value overwrites the value of the existing key because dictionaries cannot have duplicates 
student.update(add_dict)
print(student)

