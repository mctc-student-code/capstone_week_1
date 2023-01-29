from urllib import request, error
from time import sleep

# A URL for a website that we expect to be available, if we are online
url = 'https://minneapolis.edu'

seconds_to_sleep_between_checks = 3
sleep_counter = 0 # if it sleeps for 5 times, loops out and warns the user
onlineFlag = True # flag to loop out of the while loop

while onlineFlag:
    print('Checking if you are online...')
    
    try:
        # Open the URL. This will error/fail if you are not online.
        request.urlopen(url).read()
        print('You seem to be online')
    except error.URLError:
        print('You are NOT online')
        
    print(f'Sleeping for {seconds_to_sleep_between_checks} seconds...')
    print()
    sleep(seconds_to_sleep_between_checks)
    sleep_counter += 1
    
    if sleep_counter == 5: # if the program goes into sleep for the fifth time
        onlineFlag = False # makes the program stop
        print(f'Sorry, it failed to connect to the URL for {sleep_counter} times. Please check your internet connection or URL')



