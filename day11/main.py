choice = input("Is it leap year? yes/no ")
if choice == "yes":
    year = 366
else:
    year = 365
hours_in_year = year * 24
minutes_in_year = hours_in_year * 60
seconds_in_year = minutes_in_year * 60
print("This is the total amount of seconds in a year: ", seconds_in_year)
