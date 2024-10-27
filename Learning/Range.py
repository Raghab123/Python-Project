# # range()

# # Range functions return a sequence of numbers, starting from 0 (by default), and stops before a specified numbers and by default incremented by 1


# seq = range(5) # range(stop)

# for i in seq:
#     print(i)


# print()

# # range(start?, stop, step?)
# # "?" means optional

# for i in range(2,10):
#     # range(start , stop)
#     print(i)


# print()
# seq = range(2,10,2) # range(start,stop,step)

# for i in seq:
#     print(i)

# Print numbers from 1 to 100.

for i in range(1,101):
    if i < 100:
        print(i , end = ",")
    else:
        print(i)

# Print numbers from 100 to 1.

for i in reversed(range(1, 101)):
    if i > 1:
        print(i , end = ",")
    else:
        print(i)


for i in range(100,0,-1):
    if i > 1:
        print(i , end = ",")

    else:
        print(i)

# Print the multiplication table of a number n
import time

while True:
    while True:
        try:
            x = int(input("Enter the no. whose table of multiplication that you need : "))
            break
        except:
            print("Enter an integer value only and in terms of figure. ")
            time.sleep(1)


    print(f"You have entered the number {x}")

    again = input("Do you wish to change it. Y for yes and N for no. ")

    if again.upper() in ["N", "NO"]:
        break
    elif again.isdigit():
        if x == int(again) and x != 0:
            break
    
    if again.isdigit():
        if int(again) == 0:
            print("You kidding right")
            break


while x > 0:
    try:
        iterate = int(input(f"How many multiples do you need for {x} starting from 1. "))
        time.sleep(1)
        break
    except:
        time.sleep(1)
        print("only the number like 1, 2, 3. This input only understand integer values.")

if x == 0:
    print("No wonder why the Avengers or the X-men didn't take you. And they'll take fucking anybody. You're ridiculous, immature, half wit moron.")
    time.sleep(0.1)
    print("(Slight breathing)")
    time.sleep(0.1)
    print('''I have never met a sadder, more attention starving jabbering little prick in my entire life and that says a lot cause I've alive for more than 200 fucking years and I'll tell you that bald chick was right about one thing. YOU'LL NEVER SAVE THE WORLD. YOU COULDN'T EVEN SAVE A RELATIONSHIP WITH A GODDAMN STRIPPER AND MOTHERFUCKER I WISH I COULD SAY YOU DIE ALONE BUT ITS ONE OF GOD'S BEST JOKE THAT YOU CAN'T DIE EXCEPT THAT'S ON ALL OF US. ''')
    time.sleep(0.1)
    print("(Breathing heavily)")
    time.sleep(0.1)
    print("WHAT YOU GOT NOTHING TO SAY, MOUTH !!!")
    print("All your answers are zero except for undefined numbers.")


else:
    print("Okay. Here we go. Maximum effort : ")
    time.sleep(0.5)
    for i in range(1,iterate+1):
        print(f"{x} X {i} = {x * i}")


