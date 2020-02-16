from application import app
from flask import render_template

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html',home=True)


@app.route("/login")
def login():
    return render_template('login.html',login=True)

@app.route("/courses")
def courses():
    courseData= [{
        "courseId":"1111","title":"Django",
        "desc": "Intro to Django","credits":"5", "term":"Fall, Spring"}, 
        {"courseId":"2222", "title":"Flask",
        "desc":"Intro to Python-Flask", "credits":"4","term":"Spring",
        },{"courseId":"3333","title":".Net",
        "desc": "Intro to Django","credits":"5","term":"Fall, Spring"},
        {"courseId":"2222", "title":"C#",
        "desc":"Intro to Python-Flask", "credits":"4","term":"Spring",
        },{"courseId":"5555","title":"Java",
        "desc": "Intro to Django","credits":"5","term":"Fall, Spring"},
        {"courseId":"6666", "title":"C","desc":"Intro to Python-Flask", "credits":"4","term":"Spring"}]
    print(courseData[0]["title"])
    return render_template('courses.html', courseData=courseData, courses=True)

@app.route("/register")
def register():
    return render_template('register.html', register=True)

@app.route('/enrollment')
def enrollment():
    return render_template('enrollment.html',enrollment=True)