from Databases import Thong_ke
def qr_created(session, num):
    thong_so = thong_so_details(session)
    thong_so.QR_created += num
    thong_so.QR_active += num
    session.commit()
def qr_scanned(session, num):
    thong_so = thong_so_details(session)
    thong_so.QR_scanned += num
    thong_so.QR_active -= num
    session.commit()
def qr_expired(session, num):
    thong_so = thong_so_details(session)
    thong_so.QR_active -= num
    session.commit()
def thong_so_details(session):
    return session.query(Thong_ke).filter_by(id = 1).first()