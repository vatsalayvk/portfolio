from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, TextField
from wtforms import ValidationError, validators

class ContactForm(FlaskForm):
	name = TextField("Name", [validators.Required('Please enter your name !')])
	email = TextField("Email", [validators.Required('Please enter you email address !'), validators.Email()])
	message = TextAreaField("Message", [validators.Required('Enter a message !')])
	submit = SubmitField("Send")
