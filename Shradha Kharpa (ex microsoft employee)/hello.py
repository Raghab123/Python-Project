name = input ("Enter your name: ")
name = name.strip().title()
print("hello,", name)
print("hello," ,end=" ")
print(name)
first, middle, last = name.split(" ") 
'''Problem with middle names hai. subha ko four words xa tara variable 3 assign vayera error aayeko xa. first = shova , middle = thapa , last = basnet'''
print(f"Hello {first}")