from Databases import User
from sqlalchemy import select
from sqlalchemy.orm import Session
from connect import engine
import typing
class User_db_manage:
    def __init__(self, session):
        self.session:Session = session
        #self.User_db_max = None
        self.User_db_max_find()
    def User_db_add(self, name, pwrd):
        new_user = User(
            id = self.User_db_max,
            username = name,
            password = pwrd,
        )
        self.User_db_max += 1
        self.session.add_all([new_user])
        self.session.commit()
    def User_db_max_find(self):
        self.User_db_max = self.session.scalar(select(User.id).order_by(-1*User.id))
        if self.User_db_max is None:
            self.User_db_max = 1
        else:
            self.User_db_max += 1