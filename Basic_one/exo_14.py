# Python program to calculate the number of days between two dates.
from datetime import date

def days_between_dates(date1, date2):
    return abs((date2 - date1).days)

# Sample dates
date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)

# Calculate and print the difference
difference = days_between_dates(date1, date2)
print(f"{difference} days")
