import requests

question = input('Enter your question for the magic 8 ball: ')

# url doesn't work anymore - heroku is not free anymore
magic_8_ball_url = f'https://8ball.delegator.com/magic/JSON/{question}'
# important to not is how to do the try exception here.
try:
    response = requests.get(magic_8_ball_url).json()
    answer = response['magic']['answer']
    print(f'The magic 8 ball says...  {answer}')
except Exception as e:
    print(e)
    print('Sorry, can\'t contact the magic 8 ball right now')
