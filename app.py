from flask import Flask, redirect, render_template, url_for
from flask_httpauth import HTTPBasicAuth
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["usersDB"]
col = db["users"]

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    users = col.find()
    for user in users:
        if username == user["username"]:
            return user["password"] == password
    return False

@app.route('/')
@auth.login_required
def index():
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
