num_list = []

num_elements = int(input("How many items to be entered: "))

for _ in range(num_elements):
    num = int(input("Enter element: "))
    num_list.append(num)

num_list.sort()

smallest = num_list[0]

largest = num_list[-1]

print("The List is:", num_list)
print("The Smallest Element in this List is:", smallest)
print("The Largest Element in this List is:", largest)

