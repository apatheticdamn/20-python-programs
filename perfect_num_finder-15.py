number = int(input("Enter a number: "))
if number <= 1:
    print("Not a perfect number")
else:
    divisor_sum = 1
    for i in range(2, number):
        if number % i == 0:
            divisor_sum += i
    if divisor_sum == number:
        print(number, "is a perfect number.")
    else:
        print(number, "is not a perfect number.")
