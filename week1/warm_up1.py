from datetime import date

def getName():
    name = input('What is your name? ')
    return name

def monthBorn():
    month = input("What month were you born in? ")
    return month

def main():
    now = date.today()
    current_month = now.month # would be a number like 8 for august
    # to get month name
    current_month_name = now.strftime('%B') # use %b to get short form like Mar for march etc
    
    name = getName() # method call
    month = monthBorn()
    print(f'Hello, {name}')

    if month.lower() == current_month_name.lower():
        print('Happy birthday month') 
    
    print(f'There are {len(name)} letters in your name')

main()    