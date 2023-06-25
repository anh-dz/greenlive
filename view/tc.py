from flask import Blueprint, render_template
from control import *

thanhcong = Blueprint('thanhcong', __name__)

@thanhcong.route('/thanhcong')
def tc():
    return render_template("thanhcong.html")
