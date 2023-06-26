import time, base64, random, qrcode
from sqlalchemy.orm import Session
from sqlalchemy import select
from connect import engine
class QR_maker():
    def __init__(self, session, save_folder, web_link_qr) -> None:
        self.session:Session = session
        self.save_folder = save_folder
        self.web_link_qr = web_link_qr
    def QR_link_make(self):
        ma_hoa_don = "A1BXDD" #ma hoa don sample
        so_random = str(random.randint(10, 99))
        thoi_gian = time.asctime(time.localtime())
        ket_hop = ma_hoa_don + so_random + thoi_gian
        ket_hop = ket_hop.encode("ascii")
        ket_hop = base64.b64encode(ket_hop)
        ket_hop = ket_hop.decode("ascii")
        return ket_hop
    def QR_make(self, link, name):
        #qr_img = qrcode.make(self.web_link+link, version = 11)
        #qr_img.save(self.save_folder + name)
        print(self.web_link_qr + link)
make = QR_maker(Session(engine), "QR/", "localhost:5000/qr/")
make.QR_make(make.QR_link_make(), "QR")