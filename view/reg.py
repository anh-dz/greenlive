from flask import *
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
        if password != password_check:
            flash('Mật khẩu không trùng nhau', category='error')
        elif len(password)<=7:
            flash('Mật khẩu quá ngắn', category='error')
        else:
            signup(name, email, password, magioithieu)
            flash('Đăng kí thành công, vui lòng đặng nhập tài khoản', category='success')

    return render_template("register.html")
