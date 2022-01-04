 # Made by Kush(TalklessKush) 
  
 ​#Challenge - Write a program to print table of a given number
  
#Code - 

#Asking User for the Number
number = int(input("Enter Your Number"))

for i in range(1, 11):
	table = number*i #Multiplying the number given by the user with i
	print(number , "X" , i , "=" , table) #Printing The Table of the number given by the user
	
