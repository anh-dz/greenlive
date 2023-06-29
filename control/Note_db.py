from .Databases import Note
from .connect import engine
from sqlalchemy.orm import Session
import re
class Note_db_mn():
    def __init__(self, session) -> None:
        self.session = session
    def Note_db_add(self, items, time, location, user_id):
        note = Note(items=items, time=time, location=location, user_id=user_id)
        self.session.add(note)
        self.session.commit()
    def Note_db_scan(self, target_id):
        result = self.session.query(Note).filter(Note.user_id == target_id).all()
        dict = {'Item': [], 'Time':[], 'Location':[]}
        for note in result:
            dict['Item'].append(note.items)
            dict['Time'].append(note.time)
            dict['Location'].append(note.location)
        return dict
    def Note_db_notify(self, target_id):
        result = self.session.query(Note).filter(Note.user_id == target_id).all()
        for note in result:
            print(re.findall(r'\d+',note.time))

# mng = Note_db_mn(Session(engine))
# mng.Note_db_notify(1)
# mng.Note_db_add("Convit,Conngang,Concun", "11h 30/9/2021", "Vincom Plaza", 1)