from Databases import Seller
from sqlalchemy import select
from sqlalchemy.orm import Session

class Seller_db_manage:
    def __init__(self, session):
        self.session:Session = session
        self.Seller_db_max_find()
    def Seller_db_add(self, name, pwrd):
        new_seller = Seller(
            id = self.Seller_db_max,
            username = name,
            password = pwrd,
            qr_made = 0
        )
        self.Seller_db_max +=  1
        self.session.add_all([new_seller])
        self.session.commit()
    def Seller_db_add_qrmade(self, name, num):
        seller:Seller = self.session.query(Seller).filter_by(username = name).first()
        seller.qr_made += num
        self.session.commit()
    def Seller_db_max_find(self):
        self.Seller_db_max = self.session.scalar(select(Seller.id).order_by(-1*Seller.id))
        if self.Seller_db_max is None:
            self.Seller_db_max = 1
        else:
            self.Seller_db_max += 1