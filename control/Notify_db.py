from .Databases import Notifi, User
from sqlalchemy import select
from sqlalchemy.orm import Session
from .connect import engine
import time
import typing
class Notifi_db_mn():
    def __init__(self, session) -> None:
        self.session = session
        self.Notifi_max_db_find()
    def Notifi_db_add(self, text, user_id):
        new_noti = Notifi(
            id = self.notifi_max_db,
            text = text,
            user_id = user_id,
            time = time.asctime(time.localtime(time.time()))
        )
        self.session.add(new_noti)
        self.session.commit()
        self.notifi_max_db += 1
    def Notifi_db_return(self, target_id):
        result_dict = {"User_id": [], "Text": [], "Time": []}
        target = self.session.query(User).filter(User.id == target_id).first()
        if target is not None:
            result = self.session.query(Notifi).filter(Notifi.user_id == target_id).all()
            for his in result:
                result_dict["User_id"].append(target_id)
                result_dict["Text"].append(his.text)
                result_dict["Time"].append(his.time)
        return result_dict
    def Notifi_max_db_find(self):
        self.notifi_max_db = self.session.scalar(select(Notifi.id).order_by(-1*Notifi.id))
        if self.notifi_max_db is None:
            self.notifi_max_db = 1
        else:
            self.notifi_max_db += 1