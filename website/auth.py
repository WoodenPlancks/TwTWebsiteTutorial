from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)  # variable, file name, and name argument do not have to match.

@auth.route('/login')
def login():
	test_text = "Testing the parameter pass-in."
	return render_template('login.html', text=test_text, bool=False)

@auth.route('/logout')
def logout():
	return "<p>Log out</p>"

@auth.route('/sign-up')
def sign_up():
	return render_template('sign_up.html')
