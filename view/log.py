from flask import Blueprint, render_template, request
from control import *

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = logme(email, password)
        resp = flask.jsonify(user)
        resp.set_cookie("username", user.username)
        return resp
    return render_template("login.html")