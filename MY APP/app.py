from flask import Flask , render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime   

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/flaskDb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Creating a table
class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    uname = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    mobile = db.Column(db.Integer, unique=True, nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(5))
    role = db.Column(db.String(50), unique=True, nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.id}-{self.name}"

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("Index.html")

if __name__ == "__main__":
    app.run(debug=True)

# User Table   
# id
# Name
# Username
# password
# email
# mobile
# age
# gender
# role

