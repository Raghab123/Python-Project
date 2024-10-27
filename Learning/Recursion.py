# Recursion is a little bit difficult
# Advanced loops in simple words that can call the functions repeatedly 
# Loops and recursion both can do the same task.
# One is better than the other depending on the situation


def show (n):
    if (n == 0): # Base case
        return # Control return where return has no value
    print(n)
    show (n-1)

show(5)


# def show(n):
#     print(n)
#     show(n-1) This creates an infinte loop

# show (0)