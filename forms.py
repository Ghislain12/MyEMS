from flask import Flask, render_template
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL, Length, ValidationError 

class UserLoginForm(FlaskForm):
    username = StringField(label=('Enter Your Name:'))
    submit = SubmitField(label=('Submit'))