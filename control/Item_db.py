from .Databases import Item
from sqlalchemy.orm import Session
from .connect import engine
class Item_db_mn():
    def __init__(self, session):
        self.session = session
    def add_item(self, name, ma, giam, price):
        item = Item(name=name, code = ma, giam=giam, price=price)
        self.session.add(item)
        self.session.commit()
    def remove_item(self, item_id):
        item = self.session.query(Item).filter(Item.id == item_id).first()
        self.session.delete(item)
        self.session.commit()
    def get_item(self,item_id):
        return self.session.query(Item).filter(Item.id == item_id).first()
    def item_scan(self):
        result = self.session.query(Item).all()
        dict = {'id': [],'name': [], 'giam': [], 'price': []}
        for item in result:
            dict['id'].append(item.id)
            dict['name'].append(item.name)
            dict['giam'].append(item.giam)
            dict['price'].append(item.price)
        return dict
# item_db_manager = Item_db_mn(Session(engine))
# item_db_manager.add_item("Vouncher tại Circle K", "50%", 500)
# print(item_db_manager.item_scan())