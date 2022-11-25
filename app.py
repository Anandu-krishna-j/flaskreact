from flask import Flask,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
CORS(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todos = db.Column(db.String, unique=True, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/add",methods = ['GET', 'POST'])
def addData():
    data = request.get_json()
    result = data['todo']
    user = User(
            todos=result
        )
    db.session.add(user)
    db.session.commit()
    users = db.session.execute(db.select(User)).scalars()

    for users in users:
        print(users.todos)
    return jsonify({'status':'success'})

# @app.route("/view",methods = ['GET','POST'])
# def viewData():
#     # users = db.session.execute(db.select(User)).scalars()
#     return jsonify({'status':'success'})


if __name__ =='__main__':
    app.run(debug=True)