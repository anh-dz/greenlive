from flask import *
from datetime import datetime
from requests import request
from control import *

afteruser1 = Blueprint('afteruser1', __name__)
def trade_history():
    Trade_manager = Trade_history_user_mn(Session(engine))
    Trade_his = Trade_manager.trade_history_user_scan(current_user.id)
    thong_ke_doi_emerald = []
    for i in range(0, len(Trade_his['UserName'])):
        vatdung_dict = {'vatdung': Trade_his["ItemName"][i], 'ma':Trade_his['ma'][i], 'thoigian': Trade_his["Time"][i] , 'emerald': Trade_his["Emerald"][i]}
        thong_ke_doi_emerald.append(vatdung_dict)
    return thong_ke_doi_emerald  
# thong_ke_doi_emerald = [
#     {'vatdung': 'Mã giảm giá cửa hàng tiện lợi BigC', 'thoigian': '16h 28/3/2023', 'emerald': '-100'},
#     {'vatdung': 'Mã giảm giá bách hoá Trâu Quỳ', 'thoigian': '8h 30/5/2023', 'emerald': '-150'}
# ]
def gain_history():
    Gain_manager = History_user_mn(Session(engine))
    Gain_his = Gain_manager.history_user_scan(current_user.id)
    thong_ke_nhan_emerald = []
    for i in range(0, len(Gain_his['UserName'])):
        nhan_dict = {'magiamgia': Gain_his["BillCode"][i], 'thoigian': Gain_his["Time"][i] , 'emerald': Gain_his["Emerald"][i]}
        thong_ke_nhan_emerald.append(nhan_dict)
    return thong_ke_nhan_emerald  
# lich_su_tich_emerald = [
#     {'magiamgia': 'CJKJAKJCLKEOIW81951235', 'thoigian': '16h 28/3/2023', 'emerald': '+100'},
#     {'magiamgia': 'CJKAJCKJKDJKFJ819891235', 'thoigian': '8h 30/4/2023', 'emerald': '+150'}
# ]

def note_gain():
    note_manager = Note_db_mn(Session(engine))
    Trade_his = note_manager.Note_db_scan(current_user.id)
    thong_ke_doi_emerald = []
    for i in range(0, len(Trade_his['Item'])):
        vatdung_dict = {'mondocanmua': Trade_his["Item"][i],'thoigian': Trade_his["Time"][i] , 'diadiem': Trade_his["Location"][i]}
        thong_ke_doi_emerald.append(vatdung_dict)
    return thong_ke_doi_emerald  

@afteruser1.route('/afteruser1', methods=['POST', 'GET'])
@login_required
def au1():
    thong_ke_doi_emerald =  trade_history()
    lich_su_tich_emerald = gain_history()
    nhacnho = note_gain()
    if request.method == 'POST':
        if request.form.get('action1') == 'plus':
            print(1)
        elif  request.form.get('action2') == 'save':
            print(0)
        elif request.form.get('Logout') == "Logout":
            logout_user()
            return redirect('/login')
    return render_template("AfterUser1.html", user = current_user.username, data1 = thong_ke_doi_emerald, data2 = lich_su_tich_emerald, remind_data = nhacnho)

# @afteruser1.route('/add', methods=['POST'])
# def add():
#     # Get new row data from the form submission
#     vatdung = 'Test'
#     thoigian = 'Test2'
#     emerald = 'Test3'

#     # Create a new row dictionary
#     new_row = {'vatdung': vatdung, 'thoigian': thoigian, 'emerald': emerald}

#     # Add the new row to the data list
#     thong_ke_doi_emerald.append(new_row)

#     # Redirect back to the main page
#     return redirect('/afteruser1')


@afteruser1.route('/diem')
@login_required
def api_diem():
    qr_db_manager = QR_db_mn(Session(engine))
    qr_db_manager.QR_db_linkpoint_remove(qr_db_manager.QR_db_linkpoint_check())
    buyer_manager = Buyer_db_manage(Session(engine))
    dictionary_to_return = {
        'so_diem' : buyer_manager.Buyer_db_point(current_user.id)
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