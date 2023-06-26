from flask import Blueprint, render_template

afteruser2 = Blueprint('afteruser2', __name__)

@afteruser2.route('/afteruser2')
def au2():
    return render_template("AfterUser2.html")