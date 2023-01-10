def main():
    sentence = input('Enter a short sentence to convert to camel case: ')
    sample_special_characters = ['#','+','"'] # list of special characters to check
    list_of_words = sentence.split() # converts the sentence into a list with each word
    for special_character in sample_special_characters:
        if special_character in sentence: # checks if the sentence contains any special characters
            print("It contains invalid special characters") # prints a warning if it does
    
    if(list_of_words[0].isdigit()): # checks if the first character is a number
        print("The sentence starts with a number, the name will not be a valid variable name") # prints a warning message
    
    for index,word in enumerate(list_of_words): # loops through the list of words generated from the user entered sentence
        if index == 0: 
            camel_case = word.lower() # first word is made lower case as expected in camelCase
        else:
            camel_case += word.capitalize() # all the other words are capitalized and concatenated
    
    print(f'{sentence} in camel case: {camel_case}') # prints the camel case form of the sentence

main()