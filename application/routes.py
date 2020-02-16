from application import app
from flask import render_template
from flask import request

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html',home=True)


@app.route("/login")
def login():
    return render_template('login.html',login=True)

@app.route("/courses/")
@app.route("/courses/<term>/")
def courses(term=2020):
    courseData= [{
        "courseID":"1111","title":"Django",
        "description": "Intro to Django","credits":"5", "term":"Fall, Spring"}, 
        {"courseID":"2222", "title":"Python-Flask",
        "description":"Intro to Python-Flask", "credits":"4","term":"Spring",
        },{"courseID":"3333","title":".Net",
        "description": "Intro to .Net","credits":"5","term":"Fall, Spring"},
        {"courseID":"4444", "title":"C#",
        "description":"Intro to C#", "credits":"4","term":"Spring",
        },{"courseID":"5555","title":"Java",
        "description": "Intro to Java","credits":"5","term":"Fall, Spring"},
        {"courseID":"6666", "title":"C","description":"Intro to C", "credits":"4","term":"Spring"}]
    return render_template('courses.html', courseData=courseData, courses=True, term=term)

@app.route("/register")
def register():
    return render_template('register.html', register=True)

@app.route('/enrollment')
def enrollment():
    id = request.args.get("courseID")
    title = request.args.get("title")
    term = request.args.get("term")
    return render_template('enrollment.html',enrollment=True, data={"id":id,"title": title,"term": term})