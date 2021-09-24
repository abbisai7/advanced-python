from logging import debug
from flask import Flask,jsonify
from flask.scaffold import F

app = Flask(__name__)

customer ={
    "name":"Sai",
    "mail":"sai@email.commmmm"
}

@app.route("/")
def get_customer():
    return jsonify(customer)


if __name__ == "__main__":
    app.run(debug=True)