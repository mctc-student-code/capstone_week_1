print('Hello Capstone!')
# Variables
school = 'MCTC'
gpa = 3.7
students_in_class = 22

# indentation is super important in python

# if-statements / if-elif-else statements
if gpa == 4:
    print('WOW!')
elif gpa > 3:
    print('Awesome')
else :
    print('Cool!')

# lists
schools = ['MCTC', 'DCTC', 'North Heneppin Technical College']
if school in schools:
    print('MCTC is in list of schools')

schools.sort() # sorts in place but returns None
print(schools)

# adding element at the end of the list
schools.append('Century College')
print(schools)
schools.reverse() # reverses in place and returns None
print(schools) # the list order should have reversed now

# you can use in operator in sequences - 
# Strings, lists and keys in dictionary are sequences and in operator can be used with them

#strings
class_name = 'Software Development Capstone'
print(class_name.upper())
print(len(class_name))
print(class_name.split()) # by default splits with spaces
print(class_name.split('o')) # splits with each occurence of parameter 'o'

if 'Capstone' in class_name: # case sensitive comparison
    print("This must be the capstone")

# loops - for loops over range
for x in range(10):
    print(x)

# loops - for loops over sequence
for s in schools:
    print(s.upper())

for letter in school:
    print(letter * 10)

# useful in initializing list
data = [0] * 10
print(data)

more_data = [None] * 10
print(more_data) # you can put the values later 

# while loops

# name = input('Enter your name: ')
# while not name: # empty strings are considered false in python - not is similar to ! in other PL like Java
#     print('Please enter at least one character')
#     name = input('Enter your name: ')

# True and False and None

start_of_semester = True
winter = False

if winter:
    print('brrrr')
else:
    print('It is not winter')

# Dictionaries

class_codes = { 2905: 'Capstone', 2560: 'Web', 2545: 'Java'} 

print(class_codes[2560])

for code in class_codes:
    print(code)
    print(class_codes[code])

for code, name in class_codes.items():
    print('The class code is ' + str(code) + ' and the name is ' + name)

for code, name in class_codes.items():
    print(f'The class code is {code} and the name is {name}') # formatted string

# slicing strings , lists
schools = ['MCTC', 'DCTC', 'North Heneppin Technical College']
first_two = schools[:2] # if first is omitted, it is considered to start from 0
print(first_two)

last_school = schools[-1]
print(last_school)
last_two_schools = schools[-2:] # if last is omitted, it is considered to end at where the list ends
print(last_two_schools)

school_name = 'Minneapolis Community and Technical College'
city = school_name[:11]
print(city)

# File IO
with open('data.txt') as f: # reading file
    print(f.read())

with open('schools.txt', 'w') as f: # writing file
    for school in schools:
        f.writelines(school + '\n')

# Functions
def get_name():
    print('Hello, please enter your name!')
    name = input('Your name is:')
    return name

name = get_name()
print('Hello ' + name)