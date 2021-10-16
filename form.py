from flask import Flask, render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///text.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    desc = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Title %r>' % self.title

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

@app.route('/delete/<int:id>')
def delete(id):
    todo = User.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("Index"))

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

if __name__ == "__main__":
    app.run(debug=True, port=8000)

