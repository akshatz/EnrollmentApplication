from application import app, db
from flask import render_template, request, Response
import json
from application.models  import User, Enrollment, Course
from .forms import LoginForm, RegisterForm

# courseData = course.json[i]

@app.route("/")
# @app.route("/index/")
@app.route("/home/  ")
def home():
    return render_template('index.html',home=True)

@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form ,login=True)

@app.route("/courses/")
@app.route("/courses/<term>/")
def courses(term=2020):
    return render_template('courses.html', courseData=courseData,courses=True, term=term)

@app.route("/register/", methods=["POST"])
def register():
    form = RegisterForm()
    return render_template('register.html', title="Register", form=form, register=True)


@app.route('/enrollment/', methods=["GET", "POST"])
def enrollment():
    id = request.form.get("courseID")
    title = request.form["title"]
    term = request.form.get("term")
    return render_template('enrollment.html',enrollment=True, data={"id": id,"title": title, "term": term})

@app.route("/api/")
@app.route("/api/<idx>/")
def api(idx=None):
    if(idx==None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    return Response(json.dumps(jdata), mimetype="application/json")

@app.route('/users/')
def user():
    if User.objects.all() == None:
    # u = User(user_id=1, first_name= 'Akshat', last_name='' ,email='akshatzala@gmail.com', password='123456').save()
    # print(u)
       return render_template('register.html')
    else:
        users = User.objects.all()
        # print(users)
        return render_template("user.html", users=users)