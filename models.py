from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskname = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(200))

    def __init__(self, taskname, description):
        self.taskname = taskname
        self.description = description

