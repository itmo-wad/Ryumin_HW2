from flask import Flask, redirect, render_template, url_for
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user": "123",
    "guest": "qwe"
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return users.get(username) == password
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
