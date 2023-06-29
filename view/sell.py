from flask import *

seller = Blueprint('seller', __name__)

@seller.route('/seller', methods=['POST', 'GET'])
def au1():
    if request.method == 'POST':
        if request.form.get('action1') == 'mdh':
            tendonhang = request.form.get('tendonhang')
            madonhang = request.form.get('madonhang')
            nhapdiem = request.form.get('nhapdiem')
        elif  request.form.get('action2') == 'magiamgia':
            ma = request.form.get('ma')
            phantrammagiamgia = request.form.get('phantrammagiamgia')
    return render_template("seller.html")