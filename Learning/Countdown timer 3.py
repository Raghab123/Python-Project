import time
# Task: *Create a Countdown Timer for Days, Hours, Minutes, and Seconds*

my_time = int(input("Enter the time in seconds: ")) # int is very important here otherwise it won't work in range

for i in range( my_time ,0,-1):
    seconds = i % 60
    minutes = int(i/60)%60
    hours = int(i/3600)%24
    days = int(i/86400)
    print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) # Don't use time in my_time. Created errors here


print("Time's UP !!!")

