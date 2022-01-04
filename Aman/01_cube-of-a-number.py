# Made by Aman
# -------------Challenge-------------
# Write a code in Python to take input from a user and print the cube of that number.

n = int(input("\nPlease enter a number :\n"))

if n <= 1:
    print("Please enter a number which is positive and above 1 atleast!")

def cb(n):
    return n** 3

cube = cb(n)

print("Answer: Cube of {0} is {1}".format(n, cube1))
