from .Databases import Buyer, Trade_history_user
from .Buyer_db import Buyer_db_manage
from .Item_db import Item_db_mn
from .Trade_history_user_db import Trade_history_user_mn
from sqlalchemy.orm import Session
from .connect import engine
from flask import *
def buy(user_id, session, item_id):
    buyer_manager = Buyer_db_manage(session)
    Trade_history_user_manager = Trade_history_user_mn(session)
    item_manager = Item_db_mn(session)
    item = item_manager.get_item(item_id)
    amount = item.price
    if buyer_manager.Buyer_db_point(user_id) >= amount:
        buyer_manager.Buyer_db_add_point(user_id, -1*amount)
        Trade_history_user_manager.trade_history_user_add(-1*amount, item.name, item_id, user_id, ma = item.code)
        item_manager.remove_item(item_id)
        return 1
    else:
        flash('Không đủ Emerald để đổi', category='error')

# buy(1, Session(engine), 3)