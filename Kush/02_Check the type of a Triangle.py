# Made by Kush(TalklessKush) 

#Challenge - Write a program to check a triangle is equilateral, isosceles or scalene

#Code - 
print("Please Input Length of all sides of the Triangle ")
#Asking User to input length of all the sides of the triangle
a = int(input("First Side: "))
b = int(input("Second Side: "))
c = int(input("Third Side: "))

if a==b==c: #All Sides equal = Equilateral
	print("Its a Equilateral Triangle")
elif a==b or b==c or a==c: #Two Sides equal = Isosceles
	print("Its a Isosceles Triangle")
else:
	print("Its a Scalene Triangle") #No Side equal = Scalene
