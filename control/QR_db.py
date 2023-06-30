from .Databases import Links_point
from sqlalchemy import select
from sqlalchemy.orm import Session
from .connect import engine
import time
from .Thong_ke_Db import Thong_ke_db_mn
class QR_db_mn():
    def __init__(self, session) -> None:
        self.session:Session = session
        self.QR_db_max_find()
        self.Thong_ke_db_mnger = Thong_ke_db_mn(Session(engine))
    def QR_db_add(self, link, seller_id, point):
        new_QR = Links_point(
            address = link,
            start = time.time(),
            seller_id = seller_id,
            point = point
        )
        self.session.add(new_QR)
        self.session.commit()
        self.QR_db_max+=1
    def QR_db_max_find(self):
        self.QR_db_max = self.session.scalar(select(Links_point.id).order_by(-1*Links_point.id))
        if self.QR_db_max is None:
            self.QR_db_max = 1
        else:
            self.QR_db_max += 1
    def QR_db_linkpoint_remove(self, delete_links):
        a = 0
        if delete_links is not None:    
            for link in delete_links:
                a+=1
                self.session.delete(link)
        self.session.commit()
        self.QR_db_max_find()
        self.Thong_ke_db_mnger.qr_expired(a)
    def QR_db_linkpoint_check(self):
        global session
        min_time = 30#60*60*24
        statement = select(Links_point).where(Links_point.start <= time.time() - min_time)
        return self.session.scalars(statement)
    def Qr_db_linkpoint_scanned(self, link):
        self.session.delete(link)
        self.session.commit()
        self.Thong_ke_db_mnger.qr_scanned()
# mng = QR_db_mn(Session(engine))
# mng.QR_db_linkpoint_remove(mng.QR_db_linkpoint_check())