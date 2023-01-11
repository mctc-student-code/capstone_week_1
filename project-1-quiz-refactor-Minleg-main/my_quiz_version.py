"""
Project 1: User is given quiz on either art or space topic and their quiz result is printed. 
"""
def main():
    topic = chooseGenre() # user is prompted to choose their topic of interest
    # dictionary to store questions and answers as key value pairs
    art_questions_answer = {'Who painted the Mona Lisa?': 'Leonardo Da Vinci', 
                            'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz lazuli',
                            'Anish Kapoor\'s bean-shaped Cloud Gate sculpture is a landmark of which city?': 'Chicago'}

    space_questions_answer = {'Which planet is closest to the sun?': 'Mercury',
                              'Which planet spins in the opposite direction to all the others in the solar system?': 'Venus',
                              'How many moons does Mars have?': '2'}
    
    number_of_art_questions = len(art_questions_answer) # gets the number of questions for arts topic
    number_of_space_questions = len(space_questions_answer) # gets the number of questions for space topic

    if topic == 'art': 
        total = questions(art_questions_answer) # user is asked the questions on the topic and their result is stored in total variable
        output(topic,total,number_of_art_questions) # output is printed
    else : 
        total = questions(space_questions_answer) # questions asked on space topic and result is obtained in total
        output(topic,total,number_of_space_questions) # their quiz result is printed

def chooseGenre(): # method for user to choose the topic for quiz, either art or space
    genre = input("Would you like art, or space questions ? : ")
    if(genre.lower() == 'art'):
        return 'art'
    elif(genre.lower() == 'space'):
        return 'space'
    else:
        return chooseGenre() # if user enters an invalid options, the questions is asked again until user selects a valid option

def questions(question_answer_dictionary): # method to ask user the questions related to the topic and return their quiz score
    total = 0  # to store the number of questions the user got correct
    for key,value in question_answer_dictionary.items(): # loops the questions dictionary
        user_answer = input(key + ': ')
        if user_answer.lower() == value.lower(): # user can answer in any case and the answer would be correct irrespective of the case
            total = total + 1
        else:
            print(f'Sorry, the correct answer is {value}') # prints message for incorrect answers
    return total

def output(topic,total,number_of_questions): # outputs the total
    print(f'Your total score on {topic} questions is {total} out of {number_of_questions}')

main()