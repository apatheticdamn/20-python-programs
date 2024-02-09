num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

max_value = max(num1, num2)
lcm = max_value

while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += max_value
print("The lcm of {} and {} is {}".format(num1,num2,lcm))
