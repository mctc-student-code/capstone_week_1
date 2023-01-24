"""
Write a program that turns a sentence into camel case. The first word is lowercase, the rest of the words have their initial letter capitalized, and all of the words are joined together. For example, with the input "fOnt proCESSOR and ParsER", your program will output "fontProcessorAndParser". 

Optional extra question: print a warning message if the input will not produce a valid variable name. You don't need to be exhaustive in checking, but test for a few common issues, such as starting with a number, or containing invalid characters such as # or + or ".  Or, would it be easier to check that the name only contains valid characters?

Test your program with different example inputs, and comment your code. 
"""

def main():
    banner()
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
    banner()
    
def banner():
    print('\n' + '#' * 50 + '\n')
    

main()