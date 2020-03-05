from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo
from application.models import User

class LoginForm(FlaskForm):
    email           = StringField("Email",validators=[DataRequired()])
    password        = StringField("Password", validators=[DataRequired(), Length(min=6, max=50)])
    remember_me     = BooleanField("Remember Me")
    submit          = SubmitField("Login")
    
class RegisterForm(FlaskForm):
    email               = StringField("Email",validators=[DataRequired()])
    password            = StringField("Password", validators=[DataRequired(), Length(min=6, max=30)])
    password_confirm    = StringField("Confirm Password", validators=[DataRequired(), Length(min=6, max=30), EqualTo('password')])
    first_name          = StringField("First Name")
    last_name           = StringField("Last Name") 
    submit              = SubmitField("Register now")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user:
            print(user)
            raise ValidationError("Email is already in use. Choose another one.")