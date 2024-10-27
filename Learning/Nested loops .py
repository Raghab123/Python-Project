'''Nested loop is a loop within another loop (outer,inner)
                     outer loop:
                             inner loop:'''

print("Code no. 1")
for x in range(1,10):
    print(x) # no "end" function here so the output is printed on the nextline
print()
print()


print("Code no. 2")
for x in range(1,10):
    print(x, end="") # end causes to print the following output in the same line
print() # Move to the next line. Creating line gaps in the output. Otherwise code 2 and 3 will be in the same line.
print()


print("Code no. 3")
for x in range(3): # starting from zero but not including three but three times or three numbers. 🤣
    for y in range(1,10): # For nested loop we need differnet variables to avoid problems.
        print(y, end=" ")
    print() # This must be before the print("---") else the --- will be in the same line as 1 2 3 4 5 6 7 8 9 ---
    if x < 2:
        print("---")
print()
print()



print("Code no. 4")
# Example with the same variable in nested loops
# This will produce the same output for each iteration of the outer loop
for x in range(3):  # Outer loop
    for x in range(1, 4):  # Inner loop using the same variable
        print(x, end=" ")
    print()  # Newline after each inner loop completes
print()


# Output:
# 1 2 3 
# 1 2 3 
# 1 2 3 

# Explanation:
# The inner loop resets 'x' to 1 at the start of each iteration, so it prints 1 2 3 each time.
# The outer loop's variable 'x' is overwritten by the inner loop, but since the inner loop starts from 1 each time, the output remains consistent.
# Outer loop starts with x = 0.

# Inner loop runs, reassigning x to 1, 2, and 3.

# Inner loop completes, control returns to the outer loop.

# Outer loop continues with x = 1 (the next value in range(3)).



print("Code no. 5")
# Example with different variables in nested loops
# This will produce different outputs for each iteration of the outer loop
for i in range(3):  # Outer loop
    for j in range(i, i + 3):  # Inner loop with a different variable
        print(j, end=" ")
    print()  # Newline after each inner loop completes
print()


# Output:
# 0 1 2 
# 1 2 3 
# 2 3 4 

# Explanation:
# The outer loop variable 'i' changes with each iteration.
# The inner loop starts from 'i' and goes to 'i + 2', producing different outputs for each iteration of the outer loop.
# This output is differnet from the previous output as the inner loop output is dependent on the outer loop value too. Else it would have been the same

