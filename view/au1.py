from flask import *
from datetime import datetime
from requests import request
from control import *

afteruser1 = Blueprint('afteruser1', __name__)

# thong_ke_doi_emerald = [
#     {'vatdung': 'Mã giảm giá cửa hàng tiện lợi BigC', 'thoigian': '16h 28/3/2023', 'emerald': '-100'},
#     {'vatdung': 'Mã giảm giá bách hoá Trâu Quỳ', 'thoigian': '8h 30/5/2023', 'emerald': '-150'}
# ]

lich_su_tich_emerald = [
    {'magiamgia': 'CJKJAKJCLKEOIW81951235', 'thoigian': '16h 28/3/2023', 'emerald': '+100'},
    {'magiamgia': 'CJKAJCKJKDJKFJ819891235', 'thoigian': '8h 30/4/2023', 'emerald': '+150'}
]

nhacnho = [
    {'mondocanmua': 'Thịt chó', 'thoigian': '16h 28/3/2023', 'diadiem': 'AEON Mall LB'},
    {'mondocanmua': 'Mắm tôm', 'thoigian': '8h 30/4/2023', 'diadiem': 'AEON Mall LB'}
]

@afteruser1.route('/afteruser1')
def au1():
    return render_template("AfterUser1.html", data1 = thong_ke_doi_emerald, data2 = lich_su_tich_emerald, remind_data = nhacnho)

@afteruser1.route('/add', methods=['POST'])
def add():
    # Get new row data from the form submission
    vatdung = 'Test'
    thoigian = 'Test2'
    emerald = 'Test3'

    # Create a new row dictionary
    new_row = {'vatdung': vatdung, 'thoigian': thoigian, 'emerald': emerald}

    # Add the new row to the data list
    thong_ke_doi_emerald.append(new_row)

    # Redirect back to the main page
    return redirect('/afteruser1')


@afteruser1.route('/diem')
def api_diem():
    dictionary_to_return = {
        'so_diem' : so_diem
    }

    return jsonify(dictionary_to_return)

# def updateTableDoiEmerald():
#     @afteruser1.route('/vatdung')
#     def fvatdung():
#         vat_dung = 'Mã giảm giá cửa hàng tiện lợi CircleK'
#         dictionary_vatdung = {
#             vat_dung : vat_dung
#         }
#     def fthoigian():
#         thoi_gian = '16h 28/3/2023'
#         dictionary_thoigian = {
#             thoi_gian : thoi_gian
#         }
#     def fdiem():
#         emerald = '-100'
#         dictionary_diem = {
#             emerald : emerald
#         }

#     def smadonhang():
#         ma_don_hang = 'CJAJifqjojIEWJ'
#         dictionary_madonhang = {
#             ma_don_hang : ma_don_hang
#         }
#     def sthoigian():
#         thoi_gian = '16h 28/3/2023'
#         dictionary_thoigian = {
#             thoi_gian : thoi_gian
#         }
#     def sdiem():
#         emerald = '+100'
#         dictionary_diem = {
#             emerald : emerald
#         }

#     dictionary_to_return = None
#     return jsonify(dictionary_to_return)