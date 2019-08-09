from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class UserForm(FlaskForm):
    name = StringField("Username:", [validators.Length(min=2)])
    email = StringField("Email:", [validators.Length(min=2)])
 
    class Meta:
        csrf = False
