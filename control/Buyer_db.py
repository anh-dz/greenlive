from .Databases import Buyer
from sqlalchemy import select
from sqlalchemy.orm import Session
from .connect import engine
class Buyer_db_manage:
    def __init__(self, session):
        self.session:Session = session
        self.Buyer_db_max_find()
    def Buyer_db_add(self, user_id):
        new_Buyer = Buyer(
            id = self.Buyer_db_max,
            user_id = user_id,
            point_gained = 0
        )
        self.Buyer_db_max +=  1
        self.session.add_all([new_Buyer])
        self.session.commit()
    def Buyer_db_add_point(self, id, num):
        buyer:Buyer = self.session.query(Buyer).filter_by(user_id = id).first()
        if buyer is not None:
            buyer.point_gained += num
            self.session.commit()
    def Buyer_db_max_find(self):
        self.Buyer_db_max = self.session.scalar(select(Buyer.id).order_by(-1*Buyer.id))
        if self.Buyer_db_max is None:
            self.Buyer_db_max = 1
        else:
            self.Buyer_db_max += 1
    def Buyer_db_point(self, target_id):
        return self.session.query(Buyer).filter(Buyer.user_id == target_id).first().point_gained
