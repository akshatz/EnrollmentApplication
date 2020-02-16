from application import app

@app.route("/")
@app.route("/home")
def index():
    return '<h1>Hello Earth!!!</h1>'