# CRUD application in Flask

Introduction
>  In the application we are performing basic CRUD(Create, Read, Uodate, Delete) Operating using Flask.
<br>


<img align="center" src="https://github.com/rajansahu713/CRUD-application-in-Flask/blob/main/images/Screenshot%20(413).png" width="500" height="350">

<br><br>
And I also added the requirement.txt file in respo please check it and install all the dependancy to run the application. 
<br>

> Step1: 

      1. Import all the requirements
      2. Sqlalchemy is sqlite connector use to communicate with sqlite database. 

```python
from flask import Flask, render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
```

> Step2: <br>
    1. Initializing instance of flask app by declearing 
```python
app = Flask(__name__)
```
<br></br>
> Step3:<br>
    1. Creating Database
```python 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///text.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
```
<br></br>
Step4:<br>
    1. moving a step ahead by creating our model
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    desc = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Title %r>' % self.title
```

Step5:<br>
    1. This is use route to fetch all the resources or inserting a new resource to it.
    2. "index.html" is use as to show all the resources and also use to insert a new resources to table.
```python
@app.route('/', methods=['GET', 'POST'])
def Index():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        user = User(title=title, desc=desc)
        db.session.add(user)
        db.session.commit()
        
    user = User.query.all() 
    return render_template('index.html', user=user)
```

    3. This route is used to delete particular resource from table

```python
@app.route('/delete/<int:id>')
def delete(id):
    todo = User.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("Index"))
```
<br></br>
    4. The below route is used to update the resource of the table
```python
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = User.query.filter_by(id=id).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for("Index"))
        
    todo = User.query.filter_by(id=id).first()
    return render_template('update.html', todo=todo)
```
<br></br>
step6:<br>
    1. hosting crud application localhost 8000 port
```python
if __name__ == "__main__":
    app.run(debug=True, port=8000)
```
 
