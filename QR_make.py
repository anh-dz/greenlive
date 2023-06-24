import qrcode
from flask import Flask
import random
import time
import base64
from sqlalchemy.orm import Session
from sqlalchemy import select
from Databases import Links_point, Seller, Thong_ke
from connect import engine
from Thong_ke_Db import qr_created, qr_scanned, qr_expired, thong_so_details
global session, QR_db_max_id
web_main_link = "localhost:5000/"
#tạo phần chuỗi sau của link VD: /1231023. Dùng để gắn vào chuỗi link chính của web
def qr_link_make():
    link_goc = r"/"
    #tphan làm link được mã hóa
    ma_hoa_don = "A1BXDD"
    so_random = str(random.randint(10, 99))
    thoi_gian = time.asctime(time.localtime())
    #mã hóa chuỗi kết hợp từ 3 thành phần trên
    ket_hop = ma_hoa_don + so_random + thoi_gian
    ket_hop = ket_hop.encode("ascii")
    ket_hop = base64.b64encode(ket_hop)
    ket_hop = ket_hop.decode("ascii")
    #trả về theo đúng định dạng
    return link_goc+ket_hop
# qr_make() ghép link chính của web và link đuôi, và tạo ra qr xuất ra đặt tên là tham số name
def qr_make(link, name):
    global web_main_link,session
    qr_img = qrcode.make(web_main_link+"qr"+link, version = 11)
    qr_img.save("QR/" + name)
    QR_db_linkpoint_add(QR_db_max_id, link)
    qr_created(session, 1)
#tạo ra web và cho chạy. Phần web.route(link) tạo ra một trang cho link tương ứng với trong qr
def qr_web_make(link):
    web = Flask(__name__)
    @web.route(link)
    def qr_web():
        return "<h1>+1 coin </h1> <h1>Thanks for using</h1>"
    web.run()
#Ket noi voi database
def QR_db_connect():
    global session
    session = Session(bind = engine)
    session.autoflush = True
#Tim id lon nhat hop ly de bat dau trong QR database(vì đặt thuộc tính id của bảng link_point là primary key, nghĩa là ko thể
#bị trùng bởi một id có giá trị như nhau khác trong bảng)
def QR_db_max_id_find():
    global QR_db_max_id
    QR_db_max_id = session.scalar(select(Links_point.id).where(Links_point.id > 0).order_by(-1*Links_point.id))
    if QR_db_max_id is None:
        QR_db_max_id = 1
    else:
        QR_db_max_id += 1
#them vao database link point
def QR_db_linkpoint_add(id, link):
    global session, web_main_link, QR_db_max_id
    link_point = Links_point(
        id = id,
        address = web_main_link + "qr" + link,
        start = int(time.time()),
        seller_id = 1   
    )
    session.add_all([link_point])
    session.commit()
    QR_db_max_id += 1
#xoa row khoi database link_points
def QR_db_linkpoint_remove(delete_links):
    global session
    a = 0
    if delete_links is not None:    
        for link in delete_links:
            a+=1
            session.delete(link)
    qr_expired(session, a)
    session.commit()
    QR_db_max_id_find()
#check link het han sau min_time giờ kể từ khi bắt đầu thêm vào database
def QR_db_linkpoint_check():
    global session
    min_time = 1#60*60*24
    statement = select(Links_point).where(Links_point.start <= time.time() - min_time)
    return session.scalars(statement)
QR_db_connect()
QR_db_max_id_find()
link = qr_link_make()
qr_make(link, link[1::]+".png")