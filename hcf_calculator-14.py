num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

min_value = min(num1, num2)
hcf = 1
for i in range(1, min_value + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print("The hcf is", hcf)

