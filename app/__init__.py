from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

from config import CONNECT_STRING

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = CONNECT_STRING
app.config['SECRET_KEY'] = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

db = SQLAlchemy(app)

from app import models
db.create_all()
from app import routes

@app.route('/')
def index():
    return render_template('index.html')
