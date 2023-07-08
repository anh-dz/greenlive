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
            maker = QR_maker(Session(engine), "control/QR/", f"{running}/qr/")
            maker.QR_full_make(seller_id = 1, point = nhapdiem, mdh = madonhang)
            data = {
                'img' : maker.getname()
            }
            thong_ke_manager.bill_add()
            return redirect(url_for('thanhcong.tc', **data))
        elif  request.form.get('action2') == 'magiamgia':
            ma = request.form.get('ma')
            phantrammagiamgia = request.form.get('phantramgiamgia')
            gia = request.form.get('emerald')
            location = request.form.get('location')
            item_manager.add_item(name = location, ma = ma, giam = phantrammagiamgia, price=gia)
    return render_template('seller.html', qr_created = thongke.QR_created, qr_scanned = thongke.QR_scanned, qr_active = thongke.QR_active, bill_made = thongke.bill_made)
@seller.route('/qr/<name>')
@login_required
def qr(name):
    # qr_link_onweb("localhost:5000" + request.path, Session(engine))
    qr_link_onweb(running + request.path, Session(engine))
    return redirect('/afteruser1')