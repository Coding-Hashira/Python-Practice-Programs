# Made by Kush(TalklessKush) 

#Challenge - Write a program using function to convert celsius to fahrenheit

#Code - 
def farh(cel):
	return (cel * (9/5)) + 32 #Creating a Function to convert celcius to Fahrenheit	
c = 45
f = farh(c)
print("Fahrenheit Temperature of " + str(c) + " " "is" + " " + str(f)) #Printing the converted Temperature