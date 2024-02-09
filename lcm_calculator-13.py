num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

max_value = max(num1, num2)
lcm = max_value
if lcm % num1 == 0 and lcm % num2 == 0:
    quit()
lcm += max_value
print("The lcm is", lcm)



