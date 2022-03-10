from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# gives things specific to user logins. Our User class needs to import from UserMixin

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	firstName = db.Column(db.String(255))
	email = db.Column(db.String(255), unique=True)
	password = db.Column(db.String(255))
	notes = db.relationship("Note")


class Note(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(16383))
	date = db.Column(db.DateTime(timezone=True), default=func.now())
	author = db.Column(db.Integer, db.ForeignKey("user.id"))
	# Store a parent key on the child objects.
	# ForeignKey is used only for one to many relationships; in this case, one user, many notes
