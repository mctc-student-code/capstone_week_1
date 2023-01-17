# Tuples - immutable - can't be changed or modified after declaration

city_state = [('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA')] # list of tuples containing city and the state 
print(len(city_state))

first_city_state = city_state[0]
print(first_city_state) # gets the first element of the list

# one way to get the city and state value from the tuple
print(first_city_state[0])
print(first_city_state[1]) # any invalid index will give index out of bound error

# better way - tuple unpacking
city, state = first_city_state
print(city, state)

animals = ('lion', 'puma', 'tiger')
lion, puma, tiger = animals # unpacking works with more elements in the tuple as well
print(tiger) # only thing to make sure is to reference it correctly in the tuple and reference each element of the tuple

# tuple is useful in returning more than one values from a function
def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles,km

distances = get_distance() # returns a tuple
print(distances)

# tuple unpacking
miles, km = get_distance()
print(km)

