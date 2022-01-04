# Made by Jashan(Tanjiro)
# -------------Challenge-------------
# Make A Program To add all the odd numbers till a given integer 'n'
# Source: Aman

# -------------Code-------------
n = int(input())
sum=0
for i in range(n):
    if i%2!=0:
        sum = sum + i

print(sum)