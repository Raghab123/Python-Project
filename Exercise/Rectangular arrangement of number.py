rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(0,rows):
    for y in range(0,columns):
        print(symbol, end="")
    print()


rows = int(input("Enter the no. of rows: "))

while rows < 1:
    print("The rows cannot be less than 0.")
    rows = int(input("Enter the no. of rows: "))


columns = int(input("Enter the no. of columns: "))

while columns<1:
    print("The columns cannot be less than 0")
    columns = int(input("Enter the no. of columns: "))

symbol = input("Enter the symbol you would like: ")


for c in range (0,columns):
    for r in range(0,rows):
        print(symbol,end="")
    print(end="")


# This doesn't work here because columns bata iterate suru vayo vane first column matrei hunxa. Second column banaune mildena. Teshei lei garda rows lai outer loop manera iterate gareko. Euta row ma column ko entry garera new line start garera same process repeat.
# If columns were the outer loop, you'd end up stacking symbols vertically in the same column, instead of horizontally across rows