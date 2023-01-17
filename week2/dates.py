from datetime import date, time, datetime

today = date.today() 
print(today)

tomorrow = date(2023, 1, 12)
print(tomorrow)

next_week = date.fromisoformat('2023-01-16')
print(next_week)

right_now = datetime.now()
print(right_now)

print(right_now.timestamp()) # time since Jan 1 1970 UTC

# used in cases where you need to store date in database in an int form and when
# displaying the information to user, it is displayed in date form using the method below
my_date = datetime.fromtimestamp(1700000000) # converting timestamp value to a datetime value
print(my_date)


