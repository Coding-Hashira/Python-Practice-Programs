from datetime import date

y = int(input("Please enter the year (for example - 2022): \n\n"))

m = int(input("Please enter the month (for example - January is 1): \n\n"))

d = int(input("Please enter the day (for example - 1): \n\n"))


btime = date(y, m, d)


y2 = int(input("Please enter the year (for example - 2022): \n\n"))

m2 = int(input("Please enter the month (for example - January is 1): \n\n"))

d2 = int(input("Please enter the day (for example - 1): \n\n"))

atime = date(y2, m2, d2)

diff = atime - btime

print("There is a difference of "+str(diff.days)+" days")
