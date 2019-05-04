import models
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, make_response, request, session

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route("/todo")
def index_todo():
    task_list =  models.Task.query.all()
    return render_template('index.html',task_list=task_list)

@app.route("/todo/create", methods=["POST"])
def create_todo():
    taskname = request.form.get('taskname')
    description = request.form.get('description')

    task = models.Task(taskname, description)
    db.session.add(task)
    db.session.commit()

    return redirect(url_for("index_todo"))

@app.route("/todo/new")
def new_todo():
    return render_template('add.html')

@app.route("/todo/<int:task_id>")
def detail_todo(task_id):
    target_task = models.Task.query.get(task_id)
    return render_template('detail.html', target_task = target_task)

@app.route("/todo/<int:task_id>/edit")
def edit_todo(task_id):
    target_task = models.Task.query.get(task_id)
    return render_template('edit.html', target_task = target_task)

@app.route("/todo/<int:task_id>/edit" ,methods = ['POST'])
def update_todo(task_id):
    
    target_task = db.session.query(models.Task).filter_by(id=task_id).one()
    
    target_task.taskname = request.form.get('taskname')
    target_task.description = request.form.get('description')
    

    
    
       
    db.session.commit()
    
    return redirect(url_for('index_todo'))

if __name__ == '__main__':
    app.run(debug=True)