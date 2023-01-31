"""
Project 1: 
This is a quiz program where users are made to choose among a given list of topic and users try to answer on the questions about the chosen topic
and are scored accordingly. This project is flexible in the way that we can easily add new topics and the datastructure to store the questions and answer 
for the new topic and everything will operate smoothly.

All the functions have one core functionality and can operate independently in the way that, we can add more topics and more dictionaries, even
then everything will function accordingly.
"""
def main():
    # dictionary to store questions and list of correct answers as key value pairs, we can add more dictionary on other topics
    art_questions_answer = {
        'Who painted the Mona Lisa?': ['Leonardo Da Vinci', 'Da Vinci'], 
        'What precious stone is used to make the artist\'s pigment ultramarine?': ['Lapiz lazuli'],
        'Anish Kapoor\'s bean-shaped Cloud Gate sculpture is a landmark of which city?': ['Chicago'],
        'Which kid\'s TV characters are named after Renaissance artists?': ['Teenage Mutant Ninja Turtles', 'Teenage Mutant Ninja Turtle', 'Ninja Turtle', 'Ninja Turtles'],
        'The graphite in an artist\'s pencil is made of what chemical element?': ['Carbon']
    }

    space_questions_answer = {'Which planet is closest to the sun?': ['Mercury'],
                              'Which planet spins in the opposite direction to all the others in the solar system?': ['Venus'],
                              'How many moons does Mars have?': ['2','two','II'],
                              'What was the first human-made object to leave the solar system?': ['Voyager 1'],
                              'When an asteroid enters the Earth\'s atmosphere and burns up, it is known as what?': ['Meteor']}
    
    # added new sports dictionary, used to list to store the answers as there can be different versions of correct answer, like brazil or brasil 
    sports_questions_answer = {'Which gymnast is the "triple-twisting double-tucked salto backwards" skill named after?': ['Simone Biles','S Biles'],
                               'Which country has won the soccer world cup the most times?': ['Brasil','Brazil','Brazilia'],
                               'What does MLB stand for?' : ['Major League Baseball']}

    # dictionary with each topic as key and the dictionary with question and answer for the topic as the value, we can add new topics and its dictionary easily here
    # this is a more common indentation style for dictionary initalization. 
    # You don't need to use exactly this style, so long as it's readable and consistent in your code. 
    user_topic_option = {
        'art': art_questions_answer, 
        'space': space_questions_answer,
        'sport': sports_questions_answer
        }
    
    topic_option = [] # empty list to put all the topics 
    for topics in user_topic_option.keys():
        topic_option.append(topics) # adds each topic in the list
    # topic_option = ['art', 'sport', 'space']

    # Function names - good to be specific, and be consistent with naming. Either all camelCase or all snake_case.
    user_topic = choose_genre(topic_option) # user is prompted to choose their topic of interest

    # no loop needed, read the value for the user_topic key
    questions_answer = user_topic_option[user_topic]

    total = ask_questions(questions_answer) # questions function is called with the dictionary containing question and correct answer for the topic
    quiz_results(user_topic, total, len(questions_answer)) # output fun is called. 


def choose_genre(topic_option): 
    """ This method allows the user to choose the topic from a given pool of topics """
    print('Choose from following topic: \n')
    for topic in topic_option:
        print(f'* {topic} *') # prints the topics for user to choose from
    while True:
        user_topic = input('\nSelect a topic from the topic menu above: ')
        if user_topic in topic_option: # checking if topic user chose is in the list of valid topics
            return user_topic
        else :
            continue # keeps on looping if user chose a non existing topic


def ask_questions(question_answer_dictionary): # method to ask user the questions related to the topic and return their quiz score
    """ This method takes care of asking the questions on the topic and recording the score of the user as they answer each question """
    total = 0  # to store the number of questions the user got correct
    for question,correct_answer in question_answer_dictionary.items(): # loops the questions dictionary
        user_answer = input(question + ': ')
        # nice use of list comprehension!
        correct_answer_lower_case = [ answer.lower() for answer in correct_answer ] # form a new list with all correct answer in lowercase
        if user_answer.lower() in correct_answer_lower_case: # user can answer in any case and the answer would be correct irrespective of the case
            total = total + 1
        else:
            print(f'Sorry, the correct answer is {correct_answer[0]}') # prints message for incorrect answers
    return total

def quiz_results(topic,total,number_of_questions): 
    """ This method takes care of displaying the final score of the user for the chosen topic """
    print(f'Your total score on {topic} questions is {total} out of {number_of_questions}')

main() # call main function
