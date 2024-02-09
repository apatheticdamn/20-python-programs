number = int(input("Enter a number: "))

if number == 1:
    print("It is not a prime number")
elif number == 2:
    print("It's a prime number")
elif number > 1:
    for i in range(2, number):
        if number % 2 == 0:
           prime = False 
        else:
            prime = True
    if prime: print("It's a prime number")
    else: print("It's not a prime number")
