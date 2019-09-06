from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username",[validators.Length(min=2, max = 60)])
    password = PasswordField("Password", [validators.Length(min=2, max = 100)])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Name",  [validators.Length(min=2, max = 60)])
    username = StringField("Username",  [validators.Length(min=2, max = 60)])
    email = StringField("Email",  [validators.Length(min=2, max = 60)])
    password = PasswordField("Password",  [validators.Length(min=2, max = 100)])
  
    class Meta:
        csrf = False
