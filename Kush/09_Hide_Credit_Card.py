# Made by Kush(TalklessKush) 

#Challenge - Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four.

#Code- 

cc = input("Please Enter Your 16 digits long Credit Card Number: ") #Asking User for their Credit Card Number
cclen = len(cc) #Measuring Length of cc
hidecard = cclen - 4 
print("*" * (hidecard) + cc[-4:]) #Printing The Final Product