from flask import Blueprint, render_template, request
from control import *

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        logme(email, password)
    return render_template("login.html")