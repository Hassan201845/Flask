from flask import Flask, render_template, request  # NOT the same as requests 
from github_api import get_github_user  # import function to get github user info     ??
app = Flask(__name__)

@app.route('/')  # Homepage route
def homepage():
    return render_template('index.html') # returns html index we have been working on

@app.route('/get_user')
def get_user_info():
    # get user info from github api, and display on new page
    # form data is in request.args
    print('form data is', request.args) # requests.args is a dictionary

    # get info from github and display; create a template in templates.

    #username = requests.args['username']  # get username from form data
    username = request.args.get('username') #returns None if no user found
    user_info, error_message = get_github_user(username)  # TODO call function to get github user info; dictionary

    if error_message:
        return render_template('error.html', error=error_message)  # TODO pass in error message to template
    else:
        
        return render_template('github.html', user_info=user_info )  # TODO pass in user info we get from github







if __name__ == '__main__':
    app.run()