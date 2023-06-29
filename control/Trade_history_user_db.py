from .Databases import Trade_history_user, User
from sqlalchemy import select
from sqlalchemy.orm import Session
from .connect import engine
import time
import typing
class Trade_history_user_mn():
    def __init__(self, session):
        self.session:Session = session
        # self.trade_history_user_max_db_find()
    def trade_history_user_add(self, point_paid, item_name, item_id, user_id, ma):
        new_history = Trade_history_user(
        point_paid = point_paid,
        item_name = item_name,
        item_id = item_id,
        time = time.asctime(time.localtime(time.time())),
        user_id = user_id,
        ma = ma
        )
        self.session.add_all([new_history])
        self.session.commit()
        # self.trade_history_user_max_db += 1
    def trade_history_user_scan(self, target_id):
        result_dict = {"UserName": [], "ItemName": [], "Time": [], "Emerald": [], "ma":[]}
        target_type = self.session.query(User).filter(User.id == target_id).first()
        if target_type is not None and target_type.user_type == 1:
            result = self.session.query(Trade_history_user, User).filter(Trade_history_user.user_id == User.id, Trade_history_user.user_id == target_id).all()
            for his in result:
                result_dict["UserName"].append(his.User.username)
                result_dict["ItemName"].append(his.Trade_history_user.item_name)
                result_dict["Time"].append(his.Trade_history_user.time)
                result_dict["Emerald"].append(his.Trade_history_user.point_paid)
                result_dict["ma"].append(his.Trade_history_user.ma)
        return result_dict
    # def trade_history_user_max_db_find(self):
    #     self.trade_history_user_max_db = self.session.scalar(select(Trade_history_user.id).order_by(-1*Trade_history_user.id))
    #     if self.trade_history_user_max_db is None:
    #         self.trade_history_user_max_db = 1
    #     else:
    #         self.trade_history_user_max_db += 1

# mng.trade_history_user_add(-500, "Voucher", 1, 1)