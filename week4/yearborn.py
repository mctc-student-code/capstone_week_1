from datetime import datetime

current_year = datetime.today().year
oldest_year = current_year - 120 # we are assuming that older person living can be 120 years of age and not more, set up oldest birth year possible to current_year - 120

while True:
    
    try:
        birth_year = int(input('Enter the year you were born: '))
        if birth_year > current_year or birth_year < oldest_year: # if person is born after the current year or born before the oldest year possible
            raise ValueError # raises a ValueError
        break
    except ValueError:
        print(f'Please enter a number between {oldest_year} and {current_year}.')   
        
age = current_year - birth_year

print(f'Thank you, you were born in {birth_year} which makes you about {age} years of age.')