# Made by Jashan(Tanjiro)
# -------------Challenge-------------
# Make A Program To take some info like weight as input and gives output as how much water you need per day.
# Source: My Mind LOL

# -------------Code-------------
# Asking for info
weight = float(input('Please Enter Your Weight(in KGs):\n'))
age = int(input('Enter Your Age:\n')
)
weight = round(weight, 2)

# Calculations
if weight>10:
    if age<30:
        waterNeeded = round(float(weight*40), 1)
    elif 30<=age<=55:
        waterNeeded = round(float(weight*35), 1)
    elif age>55:
        waterNeeded = round(float(weight*30), 1)
    ounces= round(float(waterNeeded/28.3), 1)
    cups = int(ounces/8)
else:
    print('Enter A Valid Weight!')

print('Recommended Water Intake For You Everyday(in Ounces): ' + str(ounces) + '\n' + 'which makes upto: ' + str(cups))
