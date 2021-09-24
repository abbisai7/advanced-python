#flask

from logging import debug
import re
from flask import Flask

app = Flask(__name__) #run fake http serve on local host 5000

@app.route("/")
@app.route("/home")
def home():#web methods which can be called by http
    return "<h1>welcome to bank of america </h1>"

@app.route("/about")
def about():
    return "<h1>boa staryed in 1999</h>"

if __name__ == "__main__":
    app.run(debug = True)