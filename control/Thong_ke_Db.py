from .Databases import Thong_ke
from sqlalchemy import select
from sqlalchemy.orm import Session
from .connect import engine
class Thong_ke_db_mn():
    def __init__(self, session):
        self.session = session
    def qr_created(self,num):
        thong_so = self.thong_so_details()
        thong_so.QR_created += num
        thong_so.QR_active += num
        self.session.commit()
    def qr_scanned(self):
        thong_so = self.thong_so_details()
        thong_so.QR_scanned += 1
        thong_so.QR_active -= 1
        self.session.commit()
    def qr_expired(self,num):
        thong_so = self.thong_so_details()
        thong_so.QR_active -= num
        self.session.commit()
    def bill_add(self):
        thong_so = self.thong_so_details()
        thong_so.bill_made += 1
        self.session.commit()
    def thong_so_details(self):
        thong_so = self.session.query(Thong_ke).filter_by(id = 1).first()
        if thong_so is None:
            new_ts = Thong_ke(QR_created = 0, QR_active = 0, QR_scanned = 0, bill_made = 0)
            self.session.add(new_ts)
            self.session.commit()
            return self.thong_so_details()
        return thong_so