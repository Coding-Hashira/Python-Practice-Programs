# Made by Kush(TalklessKush) 

#Challenge - Create a function in Python that accepts a string and returns the number of vowels in that string. 

#Code - 
string = input("Enter Your String\n") #Asking user for the String
vowels = 0
for i in string:
	if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U" ):
		vowels = vowels+1
print("The Number of Vowels Are: ") #Printing the Number of vowels in the string
print(vowels)