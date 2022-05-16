from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "you don't know who i am. <br><br> <a href=/user>you want to know who i am?</>"

@app.route("/user")
def user():
    return "my name's deez"

app.run()