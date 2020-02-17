from application import app
from flask import render_template, request, Response
import json

courseData= [{
        "courseID":"1111","title":"Django","description": "Intro to Django","credits":"5", "term":"Fall, Spring"},{"courseID":"2222", "title":"Python-Flask","description":"Intro to Python-Flask", "credits":"4","term":"Spring",},{"courseID":"3333","title":".Net","description": "Intro to .Net","credits":"5","term":"Fall, Spring"},{"courseID":"4444", "title":"C#","description":"Intro to C#", "credits":"4","term":"Spring",},{"courseID":"5555","title":"Java","description": "Intro to Java","credits":"5","term":"Fall, Spring"},{"courseID":"6666", "title":"C","description":"Intro to C", "credits":"4","term":"Spring"}]

@app.route("/")
# @app.route("/index/")
@app.route("/home/  ")
def home():
    return render_template('index.html',home=True)

@app.route("/login/")
def login():
    return render_template('login.html',login=True)

@app.route("/courses/")
@app.route("/courses/<term>/")
def courses(term=2020):
    return render_template('courses.html', courseData=courseData,courses=True, term=term)

@app.route("/register/")
def register():
    return render_template('register.html', register=True)


@app.route('/enrollment', methods=["GET", "POST"])
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
