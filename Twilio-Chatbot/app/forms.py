from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,DateTimeField,TextAreaField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired,EqualTo

class ChatForm(FlaskForm):
    #initialize the form fields with datatypes
    fname = StringField('First Name', validators=[DataRequired()])
    pno = StringField('Phone Number', validators=[DataRequired()])
