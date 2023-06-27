from flask import *
from .a_log_in import *
from .a_sign_up import *
from .Buyer_db import *
from .User_db import *

def get_id():
    a = User_db_manage(Session(engine))
    idd = a.User_db_get_user('nva', 123)
    print(idd.id)
    b = Buyer_db_manage(Session(engine))
    p = b.Buyer_db_point(idd.id)
    print(p)
get_id()