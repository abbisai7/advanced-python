# flask web app with sqlAlchemy(ORM tool) to perform crud operations in databases
#pip install flask sqlalchemy flask-sqlalchemy
from enum import unique
import re
from flask import Flask
from flask import request,redirect
from flask import render_template
from flask.json import jsonify
from sqlalchemy.sql.expression import null
from flask_sqlalchemy import SQLAlchemy 
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
dbfile = "sqlite://{}".format(os.path.join(project_dir,"bookdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbfile
db = SQLAlchemy(app) # associate db with flask

#ORM=    Object Relation Mapping  (Table of Db to class of python  for performing CRUD in easy way)
#model/entity/object model

class Book(db.Model):
    title = db.Column(db.String(80),unique=True,nullable = False,PrimaryKey=True)
    def __repr__(self):
        return "Title {}".format(self.title)
    
    @app.route("/",methods=["GET","POST"])
    def home(self):
        books = None
        if request.form:
            try:
                book =Book(title = request.form.get("title"))
                db.session.add(book)
                db.session.commit() #saved in db
            
            except Exception as e:
                print(e)
        books = Book.query.all()
        return render_template("home.html",books=books)
    
    @app.route("/update",methods=["POST"])
    def update():
        pass
    
    @app.route("/delete",methods=["DELETE"])
    def delete():
        pass
    
if __name__ =="__main__":
    app.run(debug=True)
