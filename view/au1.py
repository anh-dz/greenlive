from flask import Blueprint, jsonify, render_template
import random
from datetime import datetime

afteruser1 = Blueprint('afteruser1', __name__)

@afteruser1.route('/afteruser1')
def au1():
    return render_template("AfterUser1.html")

@afteruser1.route('/datapoint')
def api_datapoint():
    so_diem = 100

    dictionary_to_return = {
        'so_diem' : so_diem
    }

    return jsonify(dictionary_to_return)