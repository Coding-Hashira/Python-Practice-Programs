from datetime import date
import calendar

y = int(input("\nPlease enter a year: \n\n"))
m = int(input("\nPlease enter a month: \n\n"))
d = int(input("\nPlease enter a date: \n\n"))

my_date = date(y, m, d)
print("\n" + calendar.day_name[my_date.weekday()] + "\n")
