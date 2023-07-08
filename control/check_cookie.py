from flask import Flask, redirect
from flask import *
from flask_login import login_user, login_required, logout_user, current_user
from .QR_db import QR_db_mn
from .Buyer_db import Buyer_db_manage
from flask_login import LoginManager
from .Databases import User, Buyer, Links_point, Seller
from .User_db import User_db_manage
from .Seller_db import Seller_db_manage
from .Buyer_db import Buyer_db_manage
from .History_user_db import History_user_mn
from .Notify_db import Notifi_db_mn
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
        login_user(user, remember=True)
        return str(1)
    else:
        return str(0)
def user_logout():
    if current_user.is_anonymous == False:
        logout_user()
def qr_link_onweb(link, session):
    link_c = session.query(Links_point).filter(Links_point.address == link).first()
    if link_c is not None:
        if current_user.is_anonymous == True:
            pass
        else:
            Buyer_manager = Buyer_db_manage(session)
            Link_point_db_manager = QR_db_mn(session)
            History_user_manager = History_user_mn(session)
            Notifi_db_manager = Notifi_db_mn(session)
            Buyer_manager.Buyer_db_add_point(current_user.id,link_c.point)
            Link_point_db_manager.Qr_db_linkpoint_scanned(link_c)
            History_user_manager.history_user_add(link_c.point, link_c.mdh, current_user.id)

            flash('Bạn vừa scan thành công 💀', category='success')

            Notifi_db_manager.Notifi_db_add(f"Bạn vừa scan thành công {link_c.point}", current_user.id)
            Notifi_db_manager.Notifi_db_add(f"Mã QR của bạn đã được scan", link_c.seller_id)
    
# vi du khi khoi tao login_manager, cho phep nhung login_user, logout_user hoat dong. khởi tạo sớm sớm
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret'
# login_manager = login_manager_create(app, Session(engine))

# muốn để một trang web cần login required vào thì thêm
# @login_required
# vào trước @app.route()
# @app.route('/login')
# def log_in():
#     rs = user_login("katori", "2")
#     return rs
# @app.route('/logout')
# def log_out():
#     user_logout()
#     return redirect('/')
# @app.route('/qr/<name>')
# @login_required
# def hetcuu(name):
#     return qr_link_onweb("localhost:5000/qr/" + name, Session(engine))
# app.run()