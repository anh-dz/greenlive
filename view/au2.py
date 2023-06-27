from flask import *
from control import *

afteruser2 = Blueprint('afteruser2', __name__)

@afteruser2.route('/afteruser2')
def au2():
    return render_template("AfterUser2.html")

@afteruser2.route('/diem')
def api_diem():
    dictionary_to_return = {
        'so_diem' : so_diem
    }

    return jsonify(dictionary_to_return)