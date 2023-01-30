def camel_case(sentence):
    
    # convert sentence into camel case and return
    sample_special_characters = ['#','+','"','@','{','}','[',']','%','$','&','|','`','!','~',';',':'] # list of special characters to check
    list_of_words = sentence.split() # converts the sentence into a list with each word
    camelCase = ''
    if len(list_of_words) == 0:
        return '' 
    for special_character in sample_special_characters:
        if special_character in sentence: # checks if the sentence contains any special characters
            print("It contains invalid special characters") # prints a warning if it does
            return None
    
    if(list_of_words[0][0].isdigit()): # checks if the first character is a number
        print("The sentence starts with a number, the name will not be a valid variable name") # prints a warning message
        return None
    
    for index, word in enumerate(list_of_words):
        if index == 0:
            camelCase += lowercase(word)
        else:
            camelCase += capitalize(word)

    
    return camelCase

def capitalize(word):
    return word.capitalize()       

def lowercase(word):
    return word.lower()
    
def main():
    sentence = input('Enter you sentence: ')
    camelcased = camel_case(sentence)
    if camelcased == None:
        print(f'Sorry you entered an invalid character in {sentence}')
    else:
        print(camelcased)


if __name__ == '__main__':
    main()