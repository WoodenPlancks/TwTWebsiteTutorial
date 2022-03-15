from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json


views = Blueprint('views', __name__)  # variable, file name, and name argument do not have to match.


@views.route('/', methods=["GET", "POST"])
@login_required
def home():
	if request.method == "POST":
		note = request.form
		note_text = note.get("note")
		new_note = Note(text=note_text, author=current_user.id)

		print("Note text is", note_text)
		print("New Note is ", new_note)

		db.session.add(new_note)
		db.session.commit()

	return render_template('home.html', user=current_user)

@views.route("/delete-note", methods = ["POST"])
def delete_note():
	data = json.loads(request.data)
	noteId = data["noteId"]
	note = Note.query.get(noteId)
	if note:
		if note.author == current_user.id:
			db.session.delete(note)
			db.session.commit()

	return jsonify({})