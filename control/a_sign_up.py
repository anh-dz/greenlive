from .User_db import User_db_manage
from .connect import engine
import sqlalchemy
from view import *
from flask import *

def signup(name, email, password, magioithieu):
    session = sqlalchemy.orm.Session(bind = engine)
    session.autoflush = True

    manager = User_db_manage(session)

    manager.User_db_add(name, password, 1)