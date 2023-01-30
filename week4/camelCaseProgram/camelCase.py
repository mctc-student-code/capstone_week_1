def camel_case(sentence):
    
    # convert sentence into camel case and return
    sample_special_characters = ['#','+','"','@','{','}','[',']','%','$','&','|','`','!','~',';',':'] # list of special characters to check
    list_of_words = sentence.split() # converts the sentence into a list with each word
    if len(list_of_words) == 0:
        return '' 
    for special_character in sample_special_characters:
        if special_character in sentence: # checks if the sentence contains any special characters
            print("It contains invalid special characters") # prints a warning if it does
            return None
    
    if(list_of_words[0][0].isdigit()): # checks if the first character is a number
        print("The sentence starts with a number, the name will not be a valid variable name") # prints a warning message
        return None
    
    for index,word in enumerate(list_of_words): # loops through the list of words generated from the user entered sentence
        if index == 0: 
            camel_case = word.lower() # first word is made lower case as expected in camelCase
        else:
            camel_case += word.capitalize() # all the other words are capitalized and concatenated
    
    return camel_case
    
def main():
    sentence = input('Enter you sentence: ')
    camelcased = camel_case(sentence)
    if camelcased == None:
        print(f'Sorry you entered an invalid character in {sentence}')
    else:
        print(camelcased)


if __name__ == '__main__':
    main()