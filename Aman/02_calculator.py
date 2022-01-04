# Made by Aman
# -------------Challenge-------------
# Make a simple calculator.

x = int(input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Sum of odd or even\n\nEnter 1 if you want to add.\n\n"))

if x == 1:

    n1 = float(input("Please enter the first number : "))
    n2 = float(input("Please enter the second number : "))

    res = n1 + n2

    print(res)


elif x == 2:
    
    n1 = float(input("Please enter the first number : "))
    n2 = float(input("Please enter the second number : "))

    res = n1 - n2

    print(res)
    

elif x == 3:
    
    n1 = float(input("Please enter the first number : "))
    n2 = float(input("Please enter the second number : "))

    res = n1 * n2

    print(res)
    

elif x == 4:
    
    n1 = float(input("Please enter the first number : "))
    n2 = float(input("Please enter the second number : "))

    quo = n1 / n2
    
    rem = n1 % n2

    print("\nAnswer: \n\nQuotient - ",quo,"\nRemainder - ",rem)
    
    
elif x == 5:
    
    oe = str(input("\nDo you want to get the sum of only odd numbers ?? (Enter yes or no)\n\n"))
    
    if oe == 'yes':
    
        n = int(input("\nPlease enter the number till which you want sum of all the odd number to be printed\n\n"))
        
        print("\n\nOdd numbers\n")
        
        sum = 0
        
        for num in range(1, n+1):
            
            if num%2!=0:
                
                sum = sum + num
                
        print(sum)
        
    elif oe == 'no':
        
        n = int(input("\nPlease enter the number till which you want sum of all the even numbers to be printed\n\n"))
        
        print("\n\nEven numbers\n")
        
        sum = 0
        
        for num in range(1, n+1):
            
            if num%2==0:
                
                sum = sum + num
                
        print(sum)
                
    else:
                
        print("\nPlease try again!!")
        
else:
    
    print("\nPlease try agin!!")
