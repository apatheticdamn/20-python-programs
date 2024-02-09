days = int(input("Enter the number of days: "))

if days < 0: print("Please enter a positive integer")
elif days == 1: print("That is 0 years, 0 months and 1 day")
else: print(f"{days} is {days//365} years, {(days%365)//30} months and {(days%365)%30} days")
