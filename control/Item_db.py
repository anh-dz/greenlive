from .Databases import Item
from sqlalchemy.orm import Session
from .connect import engine
class Item_db_mn():
    def __init__(self, session):
        self.session = session
    def add_item(self, name, seller_id, price):
        item = Item(name=name, seller_id=seller_id, price=price)
        self.session.add(item)
        self.session.commit()
    def get_item(self,item_id):
        return self.session.query(Item).filter(Item.id == item_id).first()
# item_db_manager = Item_db_mn(Session(engine))
# item_db_manager.add_item("Vouncher 50%", 1, 500)