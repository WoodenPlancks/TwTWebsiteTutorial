from flask import Blueprint, render_template

views = Blueprint('views', __name__)  # variable, file name, and name argument do not have to match.


@views.route('/')
def home():
	return render_template('home.html')
