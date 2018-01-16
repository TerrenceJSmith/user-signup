from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/')
def display_form():
    username=""
    password=""
    email="" 
    return render_template('home.html',username=username,password=password,email=email)


@app.route('/validate_user', methods=['POST'])
def validate_user():

    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verifypassword_error = ''
    email_error = ''

    if(request.method == 'POST'):

        if len(username) > 20 or len(username) < 3 or " " in username:
        
            username_error = 'Username needs to be between 3 and 20 characters with no spaces'
            username = username 
        

        if len(password) > 20 or len(password) < 3 or " " in password:
        
            password_error = 'Password needs to be between 3 and 20 characters with no spaces'
            password = "" 

        if(password != verifypassword):
            verifypassword_error="Password mismatch"

        if len(email) > 20 or len(email) < 3 or " " in email or "." not in email or "@" not in email:
        
            email_error = 'Invalid email'
            email = email


        if not username_error and not password_error and not verifypassword_error:
            return render_template("welcome.html",username=username)

    return render_template('home.html',username_error=username_error,password_error=password_error, verifypassword_error=verifypassword_error, email_error=email_error, username=username, password=password, verifypassword=verifypassword, email=email) 



if __name__ == "__main__":
    app.run()
