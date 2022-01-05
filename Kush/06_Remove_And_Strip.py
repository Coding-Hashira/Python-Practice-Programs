# Made by Kush(TalklessKush) 

#Challenge - Write a python function to remove a given word from a string and strip it at the same time

#Code - 
def remove_and_strip(string ,word): #Creating a function to remove the word
	newstr = string.replace(word , "") #Replacing/Removing word from the string
	return newstr.strip() #Returning stripped string
	
line = "        Kush is Good        "
k = remove_and_strip(line , "Kush")
print(k) #Printing the final product