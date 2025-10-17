from flask import Flask, render_template , request ,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
import os 


app = Flask(__name__)


# Get the absolute path of the current folder
basedir = os.path.abspath(os.path.dirname(__file__))

# Create a 'db' folder if it doesn't exist
db_folder = os.path.join(basedir, 'db')
os.makedirs(db_folder, exist_ok=True)

# Path to the database inside the 'db' folder
db_path = os.path.join(db_folder, 'todo.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(200),nullable = False)
    desc = db.Column(db.String(500),nullable = False)
    date_created = db.Column(db.DateTime,default= lambda:datetime.now(timezone.utc))


    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/",methods=['GET','POST','PUT','DELETE'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title = title , desc = desc)
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    
    allTodo = Todo.query.all()
    print(allTodo)
    return render_template('index.html',allTodo=allTodo)




@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route('/update/<int:sno>',methods=['GET','POST','PUT','DELETE'])
def update(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title =title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html',todo=todo)




if __name__ == "__main__":
    app.run(debug=True , port=8000)