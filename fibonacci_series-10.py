n = int(input("Enter the number of terms: "))
fib = [0,1]
for i in range(2, n+1):
    next_term = fib[-1] + fib[-2]
    fib.append(next_term)
print("Fibonacci series: ", fib)
