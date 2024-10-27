import time

my_time = int(input("Enter the time in seconds: "))

for x in range (my_time,0,-1):
    seconds = x % 60 # Mod is here just to reset the second hand to zero once 60 seconds is reached
    minutes = int(x/60) %60 # /60 converts seconds to minutes and % 60 gives the remainder
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up")


# This code is a countdown timer that converts total seconds into hours, minutes, and seconds.

# - We use x % 60 to keep the seconds hand between 0 and 59.
#   Every time we reach 60 seconds (or multiples of 60), the seconds reset to 0, and the minutes increment.
# - The minutes are calculated by dividing the total seconds by 60.
#   We use int(x / 60) % 60 to keep the minutes hand between 0 and 59.
#   Every time we reach 3600 seconds (or multiples of 3600), the minutes reset to 0, and the hours increment.
# - We don't use a modulo operation for hours because there is no limit (hours can keep increasing as no days included).
# - The time.sleep(1) ensures the countdown updates every second.
# Int is very crucial for giving whole number time

