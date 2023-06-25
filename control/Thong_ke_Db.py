from Databases import Thong_ke
from sqlalchemy import select
from sqlalchemy.orm import Session
from connect import engine
class Thong_ke_db_mn():
    def __init__(self, session):
        self.session = session
    def qr_created(self,num):
        thong_so = self.thong_so_details()
        thong_so.QR_created += num
        thong_so.QR_active += num
        self.session.commit()
    def qr_scanned(self,num):
        thong_so = self.thong_so_details()
        thong_so.QR_scanned += num
        thong_so.QR_active -= num
        self.session.commit()
    def qr_expired(self,num):
        thong_so = self.thong_so_details()
        thong_so.QR_active -= num
        self.session.commit()
    def thong_so_details(self):
        thong_so = self.session.query(Thong_ke).filter_by(id = 1).first()
<<<<<<< HEAD
        return thong_so
=======
        return thong_so
>>>>>>> 31214a3bc26fe888fd3acafeb5d466ee82a3a743
