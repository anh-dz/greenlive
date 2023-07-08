from flask import *
from control import *

afteruser2 = Blueprint('afteruser2', __name__)
Trade_manager = Trade_history_user_mn(Session(engine))
Gain_manager = Item_db_mn(Session(engine))
Buyer_manager = Buyer_db_manage(Session(engine))
Trade_manager = Trade_history_user_mn(Session(engine))
def trade_history():
    global Trade_manager
    Trade_his = Trade_manager.trade_history_user_scan(current_user.id)
    thong_ke_doi_emerald = []
    for i in range(0, len(Trade_his['UserName'])):
        vatdung_dict = {'vatdung': Trade_his["ItemName"][i],'ma':Trade_his['ma'][i], 'thoigian': Trade_his["Time"][i] , 'emerald': Trade_his["Emerald"][i]}
        thong_ke_doi_emerald.append(vatdung_dict)
    return thong_ke_doi_emerald

def gain_shop():
    global Gain_manager
    Gain_his = Gain_manager.item_scan()
    thong_ke_nhan_emerald = []
    for i in range(0, len(Gain_his['name'])):
        nhan_dict = {'cuahang': Gain_his["name"][i],'item_id': Gain_his['id'][i], 'giamgia': Gain_his["giam"][i] , 'emerald': '-' + str(Gain_his["price"][i])}
        thong_ke_nhan_emerald.append(nhan_dict)
    return thong_ke_nhan_emerald
# data = [
#     {'cuahang': 'Happy Mark', 'soluong': '30', 'giamgia': '80%', 'emerald': '-150'},
#     {'cuahang': 'Happy Mark', 'soluong': '30', 'giamgia': '60%', 'emerald': '-100'}
# ]

@afteruser2.route('/afteruser2', methods=['POST', 'GET'])
@login_required
def au2():
    data = gain_shop()
    a = len(data)
    if request.method == 'POST':
        if request.form.get("Hotro_doi") == "Hotro_doi":
            get_sotien = request.form.get("hotroemerald")
            if get_sotien.isnumeric():
                so_tien = int(get_sotien)
                global Buyer_manager, Trade_manager
                if so_tien > 0 and so_tien <= Buyer_manager.Buyer_db_point(current_user.id):
                    Buyer_manager.Buyer_db_add_point(current_user.id, -1*so_tien)
                    Trade_manager.trade_history_user_add(-1*so_tien, "Hỗ trợ", 9999999, current_user.id, ma="")
                else:
                    flash('Không đủ Emerald để quyên góp', category='error')
            else:
                flash('Vui lòng nhập số Emerald để quyên góp', category='error')
        elif request.form.get('Logout') == "Logout":
            logout_user()
            return redirect('/login')
        else:
            for i in range(1, a + 1):
                if request.form.get("button" + str(i)) == "Button_doi":
                    thong_ke_doi_emerald = trade_history()
                    item_id = data[i-1]['item_id']
                    item_buy.buy(current_user.id, Session(engine), item_id)
        data = gain_shop()
        thong_ke_doi_emerald = trade_history()
        return render_template("AfterUser2.html", user = current_user.username, data = data, data1 = thong_ke_doi_emerald)
    else:
        thong_ke_doi_emerald = trade_history()
        return render_template("AfterUser2.html", user = current_user.username, data = data, data1 = thong_ke_doi_emerald)
# onclick="deleteRow(this)"
# @afteruser2.route('/diem')
# @login_required
# def api_diem():
#     dictionary_to_return = {
#         'so_diem' : so_diem
#     }

    #return jsonify(dictionary_to_return)