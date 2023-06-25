from flask import Blueprint, render_template, request
from control import *

register = Blueprint('register', __name__)

@register.route('/register', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        password_check = request.form.get('password_check')
        magioithieu = request.form.get('magioithieu')
        signup(name, email, password, password_check, magioithieu)
    return render_template("register.html")