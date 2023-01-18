"""
Project 1: User is given quiz on either art or space topic and they are asked the questions on the topic selected. There answers
are recorded and checked with the correct answer stored in the dictionary. The user can answer in anycase and should get the point
independent of the case the user answered in.

The questions and answers for a topic are stored in a dictionary for that topic as a key-value pair.
We should be able to add more questions and answer in any of the topics in the dictionary defined and the program should 
execute correctly
"""
def main():
    # dictionary to store questions and list of correct answers as key value pairs
    art_questions_answer = {'Who painted the Mona Lisa?': ['Leonardo Da Vinci', 'Da Vinci'], 
                            'What precious stone is used to make the artist\'s pigment ultramarine?': ['Lapiz lazuli'],
                            'Anish Kapoor\'s bean-shaped Cloud Gate sculpture is a landmark of which city?': ['Chicago'],
                            'Which kid\'s TV characters are named after Renaissance artists?': ['Teenage Mutant Ninja Turtles','Teenage Mutant Ninja Turtle','Ninja Turtle','Ninja Turtles'],
                            'The graphite in an artist\'s pencil is made of what chemical element?': ['Carbon']}

    space_questions_answer = {'Which planet is closest to the sun?': ['Mercury'],
                              'Which planet spins in the opposite direction to all the others in the solar system?': ['Venus'],
                              'How many moons does Mars have?': ['2','two','II'],
                              'What was the first human-made object to leave the solar system?': ['Voyager 1'],
                              'When an asteroid enters the Earth\'s atmosphere and burns up, it is known as what?': ['Meteor']}
    
    # added new sports dictionary, used to list to store the answers as there can be different versions of correct answer, like brazil or brasil 
    sports_questions_answer = {'Which gymnast is the "triple-twisting double-tucked salto backwards" skill named after?': ['Simone Biles','S Biles'],
                               'Which country has won the soccer world cup the most times?': ['Brasil','Brazil','Brazilia'],
                               'What does MLB stand for?' : 'Major League Baseball'}

    # dictionary with each topic as key and the dictionary with question and answer for the topic as the value
    user_topic_option = {'art' : art_questions_answer, 
                         'space' : space_questions_answer,
                         'sport' : sports_questions_answer}
    
    topic_option = [] # empty list to put all the topics 
    for topics in user_topic_option.keys():
        topic_option.append(topics) # adds each topic in the dictionary of dictionary in the list
    # topic_option = ['art', 'sport', 'space']
    user_topic = chooseGenre(topic_option) # user is prompted to choose their topic of interest

    for topic, questions_answer in user_topic_option.items():
        if  user_topic == topic: # if user topic matches a topic key in the dictionary of dictionary
            total = questions(questions_answer) # questions function is called with the dictionary containing question and correct answer for the topic
            output(topic, total,len(questions_answer)) # output fun is called


def chooseGenre(topic_option): # method for user to choose the topic for quiz, either art or space
    print('Choose from following topic: ')
    for topic in topic_option:
        print(f'* {topic} *') # prints the topics for user to choose from
    while True:
        user_topic = input('Select a topic from the topic menu above: ')
        for topic in topic_option: 
            if topic == user_topic: # checking if topic user chose is in the list of valid topics
                return user_topic
            else :
                continue # keeps on looping if user chose a non existing topic


def questions(question_answer_dictionary): # method to ask user the questions related to the topic and return their quiz score
    total = 0  # to store the number of questions the user got correct
    for question,correct_answer in question_answer_dictionary.items(): # loops the questions dictionary
        user_answer = input(question + ': ')
        correct_answer_lower_case = [ answer.lower() for answer in correct_answer ] # form a new list with all correct answer in lowercase
        if user_answer.lower() in correct_answer_lower_case: # user can answer in any case and the answer would be correct irrespective of the case
            total = total + 1
        else:
            print(f'Sorry, the correct answer is {correct_answer}') # prints message for incorrect answers
    return total

def output(topic,total,number_of_questions): # outputs the total
    print(f'Your total score on {topic} questions is {total} out of {number_of_questions}')

main() # call main function
