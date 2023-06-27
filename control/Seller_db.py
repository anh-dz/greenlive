from .Databases import Seller
from sqlalchemy import select
from sqlalchemy.orm import Session
from .connect import engine
import typing
class Seller_db_manage:
    def __init__(self, session):
        self.session:Session = session
        self.Seller_db_max_find()
    def Seller_db_add(self, user_id):
        new_seller = Seller(
            id = self.Seller_db_max,
            user_id = user_id,
            qr_made = 0
        )
        self.Seller_db_max +=  1
        self.session.add_all([new_seller])
        self.session.commit()
    def Seller_db_add_qrmade(self, target_id, num):
        seller:Seller = self.session.query(Seller).filter_by(user_id = target_id).first()
        if seller is not None:
            seller.qr_made += num
            self.session.commit()
    def Seller_db_max_find(self):
        self.Seller_db_max = self.session.scalar(select(Seller.id).order_by(-1*Seller.id))
        if self.Seller_db_max is None:
            self.Seller_db_max = 1
        else:
            self.Seller_db_max += 1
    def Seller_db_qrmade(self, target_id):
        return self.session.query(Seller).filter(Seller.id == target_id).first().qr_made