'''Try It yourself
 2-8. Number Eight: Write addition, subtraction, multiplication, and division 
operations that each result in the number 8 . Be sure to enclose your operations 
in print statements to see the results . You should create four lines that look 
like this:
 print(5 + 3)
 Your output should simply be four lines with the number 8 appearing once 
on each line .
 2-9. Favorite Number: Store your favorite number in a variable . Then, using 
that variable, create a message that reveals your favorite number . Print that 
message'''

print(2+6) # The + operator adds and the print displays the output in the terminal
print(15-7) # The - operator subtracts and the print displays the output in the terminal
print(144/18) # The / operator divides and the print displays the output in the terminal
print(2*4) # The * operator multiplies and the print displays the output in the terminal

favorite_number = 7
message = "My favorite number is "
print(message + str(favorite_number))

# Favorite number is considered wrong. So favorite_number. The input of favorite_number is a integer and integer cannot be concatenated with + so we have to convert it into string by using str or we can simply do favorite_number = "7" and print(message + favorite_number)

import this # Zen of Python i.e. the principle or the philosophy