# Made by Aman
# -------------Challenge-------------
# Write a code in Python to take input from a user and print the cube of that number.

n = int(input("\nPlease enter a number :\n"))

def cbrt(n):
    return n** 3

cube1 = cbrt(n)

print("Answer: Cube of {0} is {1}".format(n, cube1))
