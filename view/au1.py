from flask import Blueprint, render_template

afteruser1 = Blueprint('afteruser1', __name__)

@afteruser1.route('/afteruser1')
def au1():
    return render_template("AfterUser1.html")