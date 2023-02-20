


# Flask web app with SqlAlchemy(ORM tool) to perform CRUD in Database
from flask import Flask
from flask import request,redirect
from flask import render_template

from flask_sqlalchemy import SQLAlchemy
import os

project_dir=os.path.dirname(os.path.abspath(__file__)) 
dbfile="sqlite:///{}".format(os.path.join(project_dir,"bookdatabase.db"))

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=dbfile
db=SQLAlchemy(app)   # db="bookdatabase.db"

#ORM=    Object Relation Mapping  (Table of Db to class of python  for performing CRUD in easy way)
#model/entity/object model

class Book(db.Model):
    title=db.Column(db.String(80),unique=True,nullable=False,primary_key=True)
    def __repr__(self):
        return "Title {}".format(self.title)

@app.route("/",methods=['GET','POST'])
def home():
    books=None
    if request.form:
        try:
            book=Book(title=request.form.get("title"))
            db.session.add(book)
            db.session.commit() #record saved in db                    
        except Exception as e:
            print(e)
    books=Book.query.all() #select * from book
    return render_template("home.html",books=books)

    
@app.route('/update',methods=["POST"])
def update():
    try:
        newtitle=request.form.get('newtitle')
        oldtitle=request.form.get('oldtitle')
        book=Book.query.filter_by(title=oldtitle).first()
        book.title=newtitle
        db.session.commit()    
    except Exception as ex:
        print('Could not update book title')
        return redirect("/")
    

@app.route('/delete',methods=["POST"])
def delete():
    title=request.form.get('title')
    book=Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")

    
if __name__ == '__main__':
    app.run(debug=True)





 



