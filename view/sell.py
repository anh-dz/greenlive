from flask import *
from control import *

seller = Blueprint('seller', __name__)

@seller.route('/seller', methods=['POST', 'GET'])
def au1():
    if request.method == 'POST':
        if request.form.get('action1') == 'mdh':
            tendonhang = request.form.get('tendonhang')
            madonhang = request.form.get('madonhang')
            nhapdiem = request.form.get('nhapdiem')
            maker = QR_maker(Session(engine), "control/QR/", "localhost:5000/qr/")
            maker.QR_full_make(seller_id = 1, point = nhapdiem, mdh = madonhang)
            data = {
                'img' : maker.getname()
            }
            return redirect(url_for('thanhcong.tc', **data))
        elif  request.form.get('action2') == 'magiamgia':
            ma = request.form.get('ma')
            phantrammagiamgia = request.form.get('phantrammagiamgia')
    return render_template("seller.html")
