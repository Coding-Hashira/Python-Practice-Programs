# Made by Aman
# -------------Challenge-------------
# Write a code in Python langauge to take input from the user and sort the string array. 

import numpy as np

n = int(input("\nPlease enter the number of length of the array:\n\n"))

arr = ["" for i in range(n)]

for i in range(n):

    arr[i] = str(input("\nValue of index " + str(i) + ":\n\n"))
    

print("\n----------------------------------------------------------------\nSorted\n")

for i in range(n):
    
    arr.sort()
    
    print(arr[i]+"\n")
