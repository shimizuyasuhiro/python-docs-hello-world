from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>online VSCodeで編集<h1>"
