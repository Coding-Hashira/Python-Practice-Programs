n = int(input("\nEnter the number of which you want to print the tables of :\n\n"))
m = int(input("\nEnter the multiplier (example - 5, 6x5 = 30) till which you want to print the tables :\n\n"))

print("\n-------------------------------\nAnswer:\n")

m = n*m

for i in range(1, m+1):
    
    if i%n == 0:
    
        print(i+"\n\n")
