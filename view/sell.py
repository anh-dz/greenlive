from flask import Blueprint, render_template

seller = Blueprint('seller', __name__)

@seller.route('/seller')
def au1():
    return render_template("seller.html")