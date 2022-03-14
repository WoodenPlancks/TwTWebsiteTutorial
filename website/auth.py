from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)  # variable, file name, and name argument do not have to match.

@auth.route('/login', methods=["GET", "POST"])
def login():
	if request.method == "POST":
		email = request.form.get("email")
		password = request.form.get("password")

		user = User.query.filter_by(email=email).first()
		if user:
			if check_password_hash(user.password, password):
				flash("Logged in successfully.", category="Success")
				login_user(user=user, remember=True)
				return redirect(url_for("views.home"))
			else:
				flash("Incorrect password. Try again.", category="Failure")
		else:
			flash("This user does not exist.", category="Failure")

	test_text = "Testing the parameter pass-in."
	return render_template('login.html', text=test_text, bool=False, user=current_user)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for("auth.login"))

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():

	if request.method == "POST":
		data = request.form
		print(data)
		email = data.get("email")
		firstName = data.get("firstName")
		password1 = data.get("password1")
		password2 = data.get("password2")

		queried_user = User.query.filter_by(email=email).first()
		if queried_user:
			flash("An account with this email already exists.", category="Failure")
		elif len(email) < 4:
			flash("Your email is too short. It must be four characters or longer.", category="Failure")
		elif len(firstName) < 2:
			flash("Your first name is too short. It must be two characters or longer", category="Failure")
		elif len(password1) < 7:
			flash("Your passwords is too short. It must be seven characters or longer.", category="Failure")
		elif password1 != password2:
			flash("Your passwords do not match.", category="Failure")
		else:
			password_hash = generate_password_hash(password1, method="sha256")
			new_user = User(email=email, firstName=firstName, password=password_hash)
			db.session.add(new_user)
			db.session.commit()

			flash("Account created!", category="Success")
			login_user(user=new_user, remember=True)
			return redirect(url_for("views.home"))

	return render_template('sign_up.html', user=current_user)
