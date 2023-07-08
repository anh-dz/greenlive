from .User_db import User_db_manage
from .connect import engine
import sqlalchemy

def logme(email, password):
    session = sqlalchemy.orm.Session(bind = engine)
    session.autoflush = True

    manager = User_db_manage(session)

    user = manager.User_db_get_user(email, password)
    if user is None:
        print("Khong the dang nhap duoc")
        return
    return user