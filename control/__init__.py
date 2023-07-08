from flask import *
from flask_login import *
#from .Databases_create import *
from .User_db import *
from .Buyer_db import *
from .a_log_in import *
from .a_sign_up import *
# from .loginReadData import *
from .History_user_db import *
# from .historyReadData import *
from .item_buy import *
from .QR_maker import *
from .check_cookie import *
from .QR_db import *
from .Note_db import *
from .Item_db import *
from .QR_maker import *

# so_diem = get_id()
# thong_ke_doi_emerald = tkdoidiem
# lich_su_tich_emerald = tktichdiem

import json

def get():
  data = open("control/Database/yourhost.json")
  resp = json.load(data)

  return resp["running"]

running = get()