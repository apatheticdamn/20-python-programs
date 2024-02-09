print("1. Area of circle\n2. Perimeter of circle")
choice = int(input("Choice: "))
if choice == 1:
    radius = int(input("Please enter the radius of the circle: "))
    area = 3.14 * (radius**2)
    print(f"The area of circle with radius {radius} is {area}.")
elif choice == 2:
    radius = int(input("Please enter the radius of the circle: "))
    perimeter = 2 * 3.14 * radius
    print(f"The perimeter of the circle with radius {radius} is {perimeter}.")
else:
    print("Please enter a vaild choice value!")



