from .Databases import User
from sqlalchemy import select
from .Buyer_db import Buyer_db_manage
from .Seller_db import Seller_db_manage
from sqlalchemy.orm import Session
class User_db_manage:
    def __init__(self, session):
        self.session:Session = session
        self.User_db_max_find()
        self.Buyer_db_manager = Buyer_db_manage(session)
        self.Seller_db_manager = Seller_db_manage(session)
    def User_db_add(self, name, pwrd, type):
        new_user = User(
            id = self.User_db_max,
            username = name,
            password = pwrd,
            user_type = type
        )
        if type == 1:
            self.Buyer_db_manager.Buyer_db_add(self.User_db_max)
        else:
            self.Seller_db_manager.Seller_db_add(self.User_db_max)
        self.User_db_max += 1
        self.session.add_all([new_user])
        self.session.commit()
    def User_db_get_user(self, name, pwd):
        return self.session.query(User).filter_by(username = name, password = pwd).first()
    def User_db_get_user_id(self, user_id):
        return self.session.query(User).filter_by(id = user_id).first()
    def User_db_max_find(self):
        self.User_db_max = self.session.scalar(select(User.id).order_by(-1*User.id))
        if self.User_db_max is None:
            self.User_db_max = 1
        else:
            self.User_db_max += 1