from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,DateTimeField,TextAreaField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired,EqualTo

class NewRec(FlaskForm):
    #initialize the form fields with datatypes
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    pno = IntegerField('Phone Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])