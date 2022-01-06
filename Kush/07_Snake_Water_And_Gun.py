# Made by Kush(TalklessKush) 

#Challenge - We all have played snake, water gun game in our childhood. If you haven't, google the rules of this game and write a Python program capable of playing this game with the user

#Code - 

import random #Importing Random Module
def game(comp, you):
	#If Two Values Are Equal, declare a tie!
	if comp == you:
		None
	#Check for all Possibilities if computer chose s
	elif comp == "s":
		if you == "w":
			return False
		elif you == "g":
			return True
			
			
	#Check for all Possibilities if computer chose w
	elif comp == "w":
		if you == "g":
			return False
		elif you == "s":		
			return True
			
  #Check for all Possibilities if computer chose g
	elif comp == "g":
		if you == "s":
			return False
		elif you == "w":
				return True

print("Computer's Turn: Snake(s) Water(w) or Gun(g)?\n")
randnum = random.randint(1 , 3)
if randnum==1:
	comp = "s"
elif randnum==2:
	comp = "w"	
elif randnum==3:
	comp = ("g")

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?\n")
a = game(comp, you)

print(f"Computer Chose {comp} ")
print(f"You Chose {you} ")
if a == None:
	print("The Game is Tied!")
elif a:
	print("You Won!")
else:
	print("You lose!")