# TODO make requests to github API
# logic for making requests to GitHub API
# details we make to githib will be here

import requests
import logging

# get github user info
def get_github_user(username):

    # 404 - username not found
    # other errors
    # success


    # return a tuple of (data, error)
    # if things work, return ( data, None)
    
    # if thngs don't , there's and error, retun( none, error)


    try:
            response = requests.get(f'https://api.github.com/users/{username}')
            

            if response.status_code ==404:
                return None, f'username{username} not found'
            response.raise_for_status()  # Raise an error for bad responses
    # make request to github api to get user info
            json_response = response.json()  # get json response from response
            user_info = extract_user_info(json_response)
            return user_info
    except Exception as e:
            logging.exception(e)
            return None, 'Error connecting to GitHub'


            response = requests.get(f'https://api.github.com/users/{username}')
        #todo error handling

            #json_response = response.json()

            
           # print('Error fetching user info:', e)
           # return None



# extract relevant user info from json response 
#              ??
def extract_user_info(json_response):

    return{
        'login': json_response.get('login'),
        'name': json_response.get('name'),
        'avatar_url': json_response.get('avatar_url'),
        'home_page': json_response.get('html_url'),
        'repos': json_response.get('public_repos')



    }