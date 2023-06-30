from .Databases import Note
from .connect import engine
from sqlalchemy.orm import Session
import time
# from win10toast_click import ToastNotifier
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
            time_strct = time.strptime(note.time, '%Hh%M %d/%m/%Y')
            time_pass = time.mktime(time_strct)
            # if (time_pass == round(time.time()) - 60*30 and time_pass <= (time.time())) or (time_pass == time.time()):
            #     toaster = ToastNotifier()
            #     toaster.show_toast(
            #         "Greenlive", # title
            #         f"Bạn có {note.items.count(',')+1} món đồ cần mua: {note.items} vào lúc {time_strct.tm_hour}:{time_strct.tm_min} ngày {time_strct.tm_mday}/{time_strct.tm_mon}/{time_strct.tm_year} tại {note.location}. Nhớ mang túi vải đi để bảo vệ môi trường.",
            #         duration=5,
            #         threaded=True,)
#buộc người dùng ghi theo format giờ phút ngaỳ tháng năm. Phút ko có phải ghi 00
# mng = Note_db_mn(Session(engine))
# while(True):
#     mng.Note_db_notify(1)
    #time.sleep(60)
# mng.Note_db_notify(1)
# mng.Note_db_add("Convit,Conngang,Concun", "11h 30/9/2021", "Vincom Plaza", 1)
# session = Session(engine)
# result = session.query(Note).filter(Note.user_id == 1).all()
# for note in result:
#     time_strct = time.strptime(note.time, '%Hh%M %d/%m/%Y')
#     time_pass = time.mktime(time_strct)
#     # if (time_pass == round(time.time()) - 60*30 and time_pass <= (time.time())) or (time_pass == time.time()):
#     toaster = ToastNotifier()
#     toaster.show_toast(
#         "Greenlive", # title
#         f"Bạn có {note.items.count(',')+1} món đồ cần mua: {note.items} vào lúc {time_strct.tm_hour}:{time_strct.tm_min} ngày {time_strct.tm_mday}/{time_strct.tm_mon}/{time_strct.tm_year} tại {note.location}. Nhớ mang túi vải đi để bảo vệ môi trường.",
#         duration=5,
#         threaded=True,)