from flask import *
from control import *

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if (email is None or password is None):
            flash('Sai tài khoản hoặc mật khẩu', category='error')
        user = logme(email, password)
        if user is None:
            flash('Sai tài khoản hoặc mật khẩu', category='error')
        else:
            resp = jsonify({ "username": user.username })
            resp.set_cookie("username", user.username)
            return resp
    return render_template("login.html")