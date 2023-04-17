print("Pick a shape (1-3):")
print("1) Square")
print("2) Rectangle")
print("3) Triangle")

shape = int(input())

if shape == 1:
    print("Enter the side length of the square:")
    side = float(input())
    area = side * side
    print("The area of the square is:", area)
elif shape == 2:
    print("Enter the length of the rectangle:")
    length = float(input())
    print("Enter the width of the rectangle:")
    width = float(input())
    area = length * width
    print("The area of the rectangle is:", area)
elif shape == 3:
    print("Enter the base of the triangle:")
    base = float(input())
    print("Enter the height of the triangle:")
    height = float(input())
    area = 0.5 * base * height
    print("The area of the triangle is:", area)
else:
    print("Invalid input. Please enter a number between 1 and 3.")
