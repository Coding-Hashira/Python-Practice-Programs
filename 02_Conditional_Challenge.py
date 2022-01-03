# Made by Jashan(Tanjiro)

# -------------Challenge-------------
# Given an integer, 'n', perform the following conditional actions:
    # 1: If 'n' is odd, print Weird
    # 2: If 'n' is even and in the inclusive range of 2 to 5, print Not Weird
    # 3: If 'n' is even and in the inclusive range of 6 to 20, print Weird
    # 4: If 'n' is even and greater than 20, print Not Weird

# -------------Code-------------

# Integer 'n'
n = int(input())

if n%2==0:
    if 2<=n<=5:
        print('Not Weird')
    if 6<=n<=20:
        print('Weird')
    if n>20:
        print('Not Weird')
else:
    print('Weird')
    