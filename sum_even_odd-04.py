n = int(input("Enter the total number of terms: "))
sum_even = sum(i for i in range(1, n + 1) if i % 2 == 0)
sum_odd = sum(i for i in range(1, n + 1) if i % 2 != 0)

print("Sum of even terms: ", sum_even)
print("Sum of odd terms: ", sum_odd)
