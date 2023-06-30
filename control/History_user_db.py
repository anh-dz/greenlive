from .Databases import History_user, User, Seller, Buyer
from sqlalchemy import select
from sqlalchemy.orm import Session
from .connect import engine
import time
import typing

class History_user_mn():
    def __init__(self, session):
        self.session:Session = session
        self.history_user_max_db_find()
    def history_user_add(self, point_gained, bill_code, user_id):
        new_history = History_user(
        id = self.history_user_max_db,
        bill_code = bill_code,
        point_gained = point_gained,
        time = time.asctime(time.localtime(time.time())),
        user_id = user_id
        )
        self.session.add_all([new_history])
        self.session.commit()
        self.history_user_max_db += 1
    def history_user_scan(self, target_id):
        result_dict = {"UserName": [], "BillCode": [], "Time": [], "Emerald": []}
        target_type = self.session.query(User).filter(User.id == target_id).first()
        if target_type is not None and target_type.user_type == 1:
            result = self.session.query(History_user, User).filter(History_user.user_id == User.id, History_user.user_id == target_id).all()
            for his in result:
                result_dict["UserName"].append(his.User.username)
                result_dict["BillCode"].append(his.History_user.bill_code)
                result_dict["Time"].append(his.History_user.time)
                result_dict["Emerald"].append(his.History_user.point_gained)
        return result_dict
    def history_user_max_db_find(self):
        self.history_user_max_db = self.session.scalar(select(History_user.id).order_by(-1*History_user.id))
        if self.history_user_max_db is None:
            self.history_user_max_db = 1
        else:
            self.history_user_max_db += 1

# mng.history_user_add(500, "Con vit", 2)