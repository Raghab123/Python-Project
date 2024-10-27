import time

my_time = int(input("Enter the time in seconds: "))
for x in reversed(range (1, my_time + 1)): #To reverse the countdown we can use reversed or change as (my_time, 0). not both
    # By adding + 1 to my_time in the range function here, you ensure that the countdown includes the value.
    print(x)
    time.sleep(1)
# This creates a delay between each number in the countdown, making it appear more like a real-time countdown.

print("Time's UP!!!")

# Same code but without reverse function

my_time = int(input("Enter the time in seconds: "))
for x in range(my_time, 0, -1):  # Start from my_time, go to 1, decrement by 1. Step is very important.
    print(x)
    time.sleep(1)

print("Time's UP!!!")
