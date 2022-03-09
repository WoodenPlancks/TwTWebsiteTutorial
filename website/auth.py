from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)  # variable, file name, and name argument do not have to match.

@auth.route('/login', methods=["GET", "POST"])
def login():
	test_text = "Testing the parameter pass-in."
	return render_template('login.html', text=test_text, bool=False)

@auth.route('/logout')
def logout():
	return "<p>Log out</p>"

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():

	if request.method == "POST":
		data = request.form
		print(data)
		email = data.get("email")
		firstName = data.get("firstName")
		password1 = data.get("password1")
		password2 = data.get("password2")

		if len(email) < 4:
			flash("Your email is too short. It must be four characters or longer.", category="Failure")
		elif len(firstName) < 2:
			flash("Your first name is too short. It must be two characters or longer", category="Failure")
		elif len(password1) < 7:
			flash("Your passwords is too short. It must be seven characters or longer.", category="Failure")
		elif password1 != password2:
			flash("Your passwords do not match.", category="Failure")
		else:
			flash("Account created!", category="Success")

	return render_template('sign_up.html')
