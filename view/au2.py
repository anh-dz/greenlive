from flask import *
from control import *

afteruser2 = Blueprint('afteruser2', __name__)

data = [
    {'cuahang': 'Happy Mark', 'soluong': '30', 'giamgia': '80%', 'emerald': '-150'},
    {'cuahang': 'Happy Mark', 'soluong': '30', 'giamgia': '60%', 'emerald': '-100'}
]

@afteruser2.route('/afteruser2')
def au2():
    return render_template("AfterUser2.html", user = 'user', data = data, data1 = thong_ke_doi_emerald)

@afteruser2.route('/diem')
def api_diem():
    dictionary_to_return = {
        'so_diem' : so_diem
    }

    return jsonify(dictionary_to_return)