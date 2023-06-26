from flask import Blueprint, render_template, request, jsonify
from control import *
from control.a_log_in import logme

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if (email is None or password is None):
            return "Khong the dang nhap duoc"
        user = logme(email, password)
        if user is None:
            return "Khong the dang nhap duoc"
        resp = jsonify({ "username": user.username })
        resp.set_cookie("username", user.username)
        return resp
    return render_template("login.html")