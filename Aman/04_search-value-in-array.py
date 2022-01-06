import numpy as np

n = int(input("\nEnter the lenght of the array:\n\n"))

arr = np.empty(n)

for i in range(0, n):

    arr[i] = int(input("\nEnter the value for index " + str(i) + ":\n\n"))


found = False

sn = int(input("\nEnter a number which you want to search :\n\n"))

for i in range(0, n):

    if sn == arr[i]:

        found = True
        index = i

if found == True:

    print("\n-------------------------------------------\n\nAnswer:\n")
    print("Found the number\n\nIndex: " + str(i) + "\nNumber: " + str(sn) + "\n")

elif found == False:

    print("-------------------------------------------\n\nAnswer:\n")
    print("Couldn't find the number " + str(sn)+"\n")
