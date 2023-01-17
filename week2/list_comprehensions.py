"""
You can always use loops andif statements in place of list comprehensions, whichever is more readable for you
But it's nice to safe typing and we will see a lot of list comprehensions in Python code
"""
# The classes a student is registered for
classes_registered = ['ITEC 1150', 'ITEC 1100', 'ENGL 1340', 'MATH 1100']

# make a list of only the ITEC classes
only_itec = [ c for c in classes_registered if c.startswith('ITEC') ] 
# you can perform operation on first c which the value you are putting in the new list, like c.lower() will make all items in lowercase
print(only_itec)

# Record temperature everyday. Record -1 if not possible to take measurement.
high_temps = [-1, 78, 72, 67, -1, 51, 87, 82, -1, 54, 67, 78, -1, 70]

# Make a list of only numbers that represent a valid temperature measurement - if we need to find an average temperature
only_real_measurements = [ temp for temp in high_temps if temp != -1]
print(only_real_measurements)

# temp is converted to celcius and restricted to two decimal point
temp_celsius = [round((temp_f - 32) * 5 / 9, 2) for temp_f in only_real_measurements] 
print(temp_celsius)


average = sum(temp_celsius) / len(temp_celsius)
print(f'The average is {average:.2f}')

strings = ['pizza', 'Beyonce', 'cat']
lengths = []

# loop version
for string in strings:
    length = len(string)
    lengths.append(length)
print(lengths)

# list comprehension version
lengths = [ len(string) for string in strings]
print(lengths)

# more list compreshension examples
original_numbers = [2,4,6]
numbers_increased_by_one = [number+1 for number in original_numbers]
print(numbers_increased_by_one)

numbers = [1, -10, 40, -6, -500, 350]
positive_numbers = [ n for n in numbers if n >= 0]
print(positive_numbers)

# combining filtering and operations
foods = ['cheese pizza', 'pepperoni pizza', 'ice cream', 'veggie pizza', 'tacos']
pizzas = [ food.upper() for food in foods if 'pizza' in food]
print(pizzas)

# Python test for membership, use in operator - python doesn't have contains() method
example = [1, 5, 10]
is_one_in_list = 1 in example # True
print(is_one_in_list)
is_seven_in_list = 7 in example # False
print(is_seven_in_list)

course = 'ITEC 1150 Programming Logic'
if '1150' in course:
    print('This is Programming Logic class')

# challenge
original = [0, 3, 4, 0, 22, 1]
non_zero_list = [ n for n in original if n != 0 ]
print(non_zero_list)

classes = ['ITEC 2560', 'BTEC 1010', 'ITEC 2905']
non_itec_classes = [ c for c in classes if 'ITEC' not in c ]
print(non_itec_classes)

# combining filtering and operations
og_list = [0,10,4,0,32]
# list with all numbers doubled, but only if number is not 0
doubled_list = [number*2 for number in og_list if number != 0]
print(doubled_list)

