from flask import *
from control import *
seller = Blueprint('seller', __name__)
item_manager = Item_db_mn(Session(engine))
thong_ke_manager = Thong_ke_db_mn(Session(engine))
@seller.route('/seller', methods=['POST', 'GET'])
def au1():
    global thong_ke_manager
    thongke = thong_ke_manager.thong_so_details()
    if request.method == 'POST':
        if request.form.get('action1') == 'mdh':
            tendonhang = request.form.get('tendonhang')
            madonhang = request.form.get('madonhang')
            nhapdiem = request.form.get('nhapdiem')
            # maker = QR_maker(Session(engine), "control/QR/", "localhost:5000/qr/")
            maker = QR_maker(Session(engine), "control/QR/", "20.205.15.33/qr/")
            maker.QR_full_make(seller_id = 1, point = nhapdiem, mdh = madonhang)
            data = {
                'img' : maker.getname()
            }
            return redirect(url_for('thanhcong.tc', **data))
        elif  request.form.get('action2') == 'magiamgia':
            ma = request.form.get('ma')
            phantrammagiamgia = request.form.get('phantramgiamgia')
            gia = request.form.get('emerald')
            location = request.form.get('location')
            item_manager.add_item(name = location, ma = ma, giam = phantrammagiamgia, price=gia)
    return render_template('seller.html', qr_created = thongke.QR_created, qr_scanned = thongke.QR_scanned, qr_active = thongke.QR_active)
@seller.route('/qr/<name>')
@login_required
def qr(name):
    # qr_link_onweb("localhost:5000" + request.path, Session(engine))
    qr_link_onweb("20.205.15.33" + request.path, Session(engine))
    return redirect('/afteruser1')