"""
Sets are unordered collection, modifiable datastructure, duplicates are not allowed
"""

cats = set() # creates an empty set
cats.add('Lion')
cats.add('Tiger')
print(cats)
cats.add('Cheetah')
print(cats)

birds = { 'owl', 'robin', 'swan'}
print(birds)
birds.add('robin') # doesn't add since it already exists
print(birds)

birds.remove('owl') # removes an element
birds.add('cardinal')
print(birds)

# looping through a set 
for bird in birds:
    print(bird)

bird_list = ['owl', 'robin', 'swan', 'eagle', 'owl', 'robin', 'swan','cardinal'] # with duplicates
# to get a bird list with no dublicate values, convert it to set and then back to a list
bird_list_no_duplicates = list(set(bird_list))
print(bird_list_no_duplicates)
