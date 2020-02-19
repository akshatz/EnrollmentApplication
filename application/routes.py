from application import app, db
from flask import render_template, request, Response, redirect, flash
import json
from application.models  import User, Enrollment, Course
from .forms import LoginForm, RegisterForm

courseData = [{"courseID": 1111, "title":"Django", "description": "Intro to Django","credits":5, "term":"Fall, Spring"},{"courseID": 2222, "title":"Python-Flask","description":"Intro to Python-Flask", "credits":4,"term":"Spring"},{"courseID": 3333, "title":".Net", "description": "Intro to .Net", "credits":5, "term":"Fall, Spring"},{"courseID": 4444, "title":"C#","description":"Intro to C#", "credits":4,"term":"Spring"},{"courseID": 5555,"title":"Java","description": "Intro to Java","credits":"5","term":"Fall, Spring"},{"courseID": 6666, "title":"C","description":"Intro to C", "credits": 4,"term":"Spring"}]

# @app.route("/index/")
@app.route("/home/")
def home():
    return render_template('index.html',home=True)

@app.route("/", methods=["GET", "POST"])
@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if  request.form.get("email") == 'akshatzala@gmail.com' and request.form.get("password") == '123456':
            flash("You are logged in successfully!!!", "success")
            return redirect("/courses/")
        else:
            flash("Sorry!!! Something went wrong.", "error")
    return render_template('login.html', title="Login", form=form ,login=True)

@app.route("/courses/")
@app.route("/courses/<term>/")
def courses(term=2020):
    return render_template('courses.html', courseData=courseData, courses=True, term=term)

@app.route("/register/", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if  request.form.get("email") == 'akshatzala@gmail.com' and request.form.get("password") == '123456' and request.form.get("first_name")== first_name and request.form.get("last_name")==last_name:
            flash("You have successfully registered!!!", "success")
            return redirect("/login/")
        else:
            flash("Sorry!!! Something went wrong.", "error")
    
    return render_template('register.html', title="Register", form=form, register=True)


@app.route('/enrollment/', methods=["GET", "POST"])
def enrollment():
    if (courses):
        id = request.form.get("courseID")
        # title = request.form["title"]
        term = request.form.get("term")
        return render_template('enrollment.html',enrollment=True, data={"id": id, "term": term})
    else:
        id = request.form.get("courseID")
        title = request.form.get["title"]
        term = request.form.get("term")
        return  render_template('enrollment.html',enrollment=True, data={"id": id, "title":None, "term": term})

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