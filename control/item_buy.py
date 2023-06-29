from .Databases import Buyer, Trade_history_user
from .Buyer_db import Buyer_db_manage
from .Trade_history_user_db import Trade_history_user_mn
from sqlalchemy.orm import Session
from .connect import engine
def buy(user_id, amount, session, item_id, item_name):
    buyer_manager = Buyer_db_manage(session)
    Trade_history_user_manager = Trade_history_user_mn(session)
    if buyer_manager.Buyer_db_point(user_id) >= amount:
        buyer_manager.Buyer_db_add_point(user_id, -1*amount)
        Trade_history_user_manager.trade_history_user_add(-1*amount, item_name, item_id, user_id)
        return 1
    else:
        return 0
buy(1, 700, Session(engine), 1, "A 50% Vouncher")