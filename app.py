from flask import Flask, request, redirect, url_for
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, PasswordField, SubmitField)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/car/", methods=['GET'])
def car():
    return render_template('car.html')

@app.route("/house/", methods=['GET'])
def house():
    return render_template('house.html')




if __name__ == "__main__":
    app.run(debug=True)

