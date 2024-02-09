number = int(input("Enter a number: "))

num_str = str(number)
num_digits = len(num_str)

sum_of_cubes = 0

for digit_char in num_str:
    digit = int(digit_char)
    sum_of_cubes += digit ** num_digits

if number == sum_of_cubes:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")

