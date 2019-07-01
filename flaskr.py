from flask import Flask, url_for, render_template, redirect, request, flash, session, escape
app = Flask(__name__)
app.secret_key = 'password'

@app.route('/')
def main_menu():
    if 'username' in session:
        return 'Logged in as %s' %escape(session['username'])
    # return render_template('menu.html')
    return render_template('menu', user=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.route('/<username>-profile', methods=['GET','POST'])
def user_profile(username):
    if request.method == 'POST':
        update_profile()
    #show the user profile for that user
    # return 'User %s' % username
    return render_template('profile.html', user=username)

@app.route('/scoreboard/<username>')
def show_rank(username):
    # return 'Ranking %d' username
    return render_template('scoreboard.html', user=username)    

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@app.route('/logout')
def logout():
    #remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('menu'))
    