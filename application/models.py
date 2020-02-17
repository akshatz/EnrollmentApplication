import flask
# from Flask import models
from application import db


class User(db.Document):
    user_id     =   db.ObjectIdField( unique=True )
    first_name  =   db.StringField( max_length=50, required=True )
    last_name   =   db.StringField( max_length=50 )
    email       =   db.StringField( max_length=50, required=True, unique=True )
    password    =   db.StringField( max_length=30, required=True, min_length= 8 )

class Course(db.Document):
    course_id   =   db.StringField(max_length=10, unique=True )
    title       =   db.StringField(max_length=100 )
    description =   db.StringField(max_length=255 )
    credits     =   db.IntField()
    term        =   db.StringField(max_length=25 ) 

class Enrollment(db.Document):
    user_id     =   db.ObjectIdField()
    course_id   =   db.StringField(max_length=10)
