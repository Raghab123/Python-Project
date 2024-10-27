# Python compound interest calculator





while True :
    p = float(input("Enter the principal amount: "))
    if p < 0 :
        print("The principal cannot be less than zero.")
    else :
        break


while True:
    r = float(input("Enter the rate of interest in per annum: "))
    if r < 0 :
        print("The rate of interest cannot be less than zero.")
    else:
        break



while True :
    t = float(input("Enter the time upto which compound interest takes place in years: "))
    if t < 0 :
     print("The time of compound interest cannot be zero or less than zero.")
    else:
        break

interest = p * pow((1 + r/100), t ) - p
amount = p * pow((1 + r/100), t )
print(f"The compound interest having principal {p} with rate of interest per annum {r} and time {t} years is "
      f"${interest:,.3f}")
print(f"The amount is ${amount:,.3f}")