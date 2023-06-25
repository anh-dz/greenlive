from Databases import User
from sqlalchemy import select
from sqlalchemy.orm import Session
class User_db_manage:
    def __init__(self, session):
        self.session:Session = session
        self.User_db_max_find()
    def User_db_add(self, name, pwrd):
        new_user = User(
            id = self.User_db_max,
            username = name,
            password = pwrd,
            point = 0
        )
        self.QR_db_max += 1
        self.session.add_all([new_user])
        self.session.commit()
    def User_db_get_user(self, name, pwd):
        return self.session.query(User).filter_by(username = name, password = pwd).first()
    def User_db_addpoint(self, name, point):
        user_scanned:User = self.session.query(User).filter_by(username = name).first()
        user_scanned.point += point
        self.session.commit()
    def User_db_max_find(self):
        self.User_db_max = self.session.scalar(select(User.id).order_by(-1*User.id))
        if self.User_db_max is None:
            self.User_db_add_db_max = 1
        else:
            self.User_db_max += 1