import time, base64, random, qrcode
from sqlalchemy.orm import Session
from sqlalchemy import select
from .connect import engine
from .Thong_ke_Db import Thong_ke_db_mn
from .QR_db import QR_db_mn
from .Seller_db import Seller_db_manage
class QR_maker():
    def __init__(self, session, save_folder, web_link_qr) -> None:
        self.session:Session = session
        self.save_folder = save_folder
        self.web_link_qr = web_link_qr
        self.QR_db_mnger = QR_db_mn(session)
        self.Thong_ke_mnger = Thong_ke_db_mn(session)
        self.Seller_db_mnger = Seller_db_manage(session)
        self.name = None
    def QR_link_make(self, mdh):
        ma_hoa_don = mdh #ma hoa don sample
        so_random = str(random.randint(10, 99))
        thoi_gian = time.asctime(time.localtime())
        ket_hop = ma_hoa_don + so_random + thoi_gian
        ket_hop = ket_hop.encode("ascii")
        ket_hop = base64.b64encode(ket_hop)
        ket_hop = ket_hop.decode("ascii")
        return ket_hop
    def QR_make(self, link, name):
        qr_img = qrcode.make(link, version = 11)
        qr_img.save(name)
        with open(name, "rb") as image_file:
            self.encoded_string = base64.b64encode(image_file.read())
    def QR_full_make(self, seller_id, point, mdh):
        link = self.QR_link_make(mdh)
        link_on_web = self.web_link_qr + link
        self.name = self.save_folder + link + ".png"
        self.QR_make(link_on_web, self.name)
        self.QR_db_mnger.QR_db_add(link_on_web,seller_id, point, mdh)
        self.Thong_ke_mnger.qr_created(1)
        self.Seller_db_mnger.Seller_db_add_qrmade(seller_id,1)
    def getname(self):
        print(self.encoded_string)
        return self.encoded_string
# maker = QR_maker(Session(engine), "control/QR/", "localhost:5000/qr/")
# maker.QR_full_make(seller_id = 1, point = 400, mdh = 'TEST')