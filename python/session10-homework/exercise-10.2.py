# factorial exercise
def recursive_factorial(num):
    if num == 0:
        return 1
    else:
        return num * recursive_factorial(num-1)

print (recursive_factorial(5))


# sum square of 2 numbers
sumSquareOf2 = lambda a, b: a**2 + b**2
print(sumSquareOf2(2,3))
