from flask import *
from control import *

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET', 'POST'])
def log():
    if current_user.is_anonymous == False:
        return redirect('/afteruser1')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if (email is None or password is None):
            flash('Sai tài khoản hoặc mật khẩu', category='error')
        user = logme(email, password)
        if user is None:
            flash('Sai tài khoản hoặc mật khẩu', category='error')
        else:
            #resp = jsonify({ "username": user.username })
            user_login(email, password)
            resp = make_response(redirect('/afteruser1'))
            resp.set_cookie("username", user.username)
            return resp
    return render_template("login.html")
@login.route('/logout')
def logout():
    user_logout()
    return redirect(url_for('login.log'))