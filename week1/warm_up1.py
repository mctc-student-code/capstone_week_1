"""
Jan 10 2023

Write a program that asks for your name and the month you were born in
Your program should print 
A greeting to you, using your name
A message with the number of letters in your name
A 'Happy birthday month!' message if you were born in January
Bonus question – can you detect if the month entered is the same as the current month, no matter when you run the program?

"""
from datetime import date

def getName(): # to get name
    name = input('What is your name? ')
    return name

def monthBorn(): # to get month there were born
    month = input("What month were you born in? ")
    return month

def main():
    now = date.today()
    # current_month = now.month # would be a number like 8 for august
    # to get month name
    current_month_name = now.strftime('%B') # use %b to get short form like Mar for march etc
    
    name = getName() # method call
    month = monthBorn()
    print(f'Hello, {name}')

    if month.lower() == current_month_name.lower(): # checks if the it's their birthday month
        print('Happy birthday month') 
    
    print(f'There are {len(name)} letters in your name')

main()    