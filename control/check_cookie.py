from flask import Flask, redirect
from flask import render_template, make_response, request
from flask_login import login_user, login_required, logout_user, current_user
from flask_login import LoginManager
from .Databases import User
from .User_db import User_db_manage
from .connect import engine
from sqlalchemy.orm import Session
def login_manager_create(app, session):
    mng = User_db_manage(session)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    @login_manager.user_loader
    def load_user(user_id):
        user = mng.User_db_get_user_id(user_id)
        return user
    @login_manager.unauthorized_handler
    def unauthorized_go_away():
        return redirect('/login')
    return login_manager
def user_login(username, password):
    mng = User_db_manage(Session(engine))
    user = mng.User_db_get_user(username, password)
    if user is not None:
        login_user(user)
        return str(1)
    else:
        return str(0)
def user_logout():
    if current_user.is_anonymous == False:
        logout_user()
# vi du khi khoi tao login_manager, cho phep nhung login_user, logout_user hoat dong. khởi tạo sớm sớm
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret'
# login_manager = login_manager_create(app, Session(engine))

# muốn để một trang web cần login required vào thì thêm
#@login_required
#vào trước @app.route()
# @app.route('/login')
# def log_in():
#     rs = user_login("katori", "2")
#     return rs
# @app.route('/logout')
# def log_out():
#     user_logout()
#     return redirect('/')
# app.run()