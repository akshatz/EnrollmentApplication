from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email       = StringField("Email",validators=[DataRequired()])
    password    = StringField("Password", validators=[DataRequired()])
    remmember_me= BooleanField("Remember Me")
    submit      = SubmitField("Login")
    
class RegisterForm(FlaskForm):
    email               = StringField("Email",validators=[DataRequired()])
    password            = StringField("Password", validators=[DataRequired()])
    password_confirm    = StringField("Confirm Password", validators=[DataRequired()])
    first_name          = StringField("Password", validators=[DataRequired()])
    last_name           = StringField("Password", validators=[DataRequired()])
    submit              = SubmitField("Register")