import flask
from User_db import User_db_manage
from connect import engine
import sqlalchemy

def run()
    app = flask.Flask(__name__)

    session = sqlalchemy.orm.Session(bind = engine)
    session.autoflush = True

    manager = User_db_manage(session)

    @app.route("/user/login")
    def user_login():
        user = manager.User_db_get_user(flask.request.json.name, flask.request.json.password) 
        if user is None:
            raise
        return { id: user.id, point: user.point }

        
        

        

        
        