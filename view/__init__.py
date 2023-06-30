from flask import Flask
from .home import homepage
from .reg import *
from .log import *
from .au1 import afteruser1
from .au2 import afteruser2
from .sell import seller
from .tc import *

def create_app(viewer):
    viewer.register_blueprint(homepage, url_prefix="/")
    viewer.register_blueprint(register, url_prefix="/")
    viewer.register_blueprint(login, url_prefix="/")
    viewer.register_blueprint(afteruser1, url_prefix="/")
    viewer.register_blueprint(afteruser2, url_prefix="/")
    viewer.register_blueprint(seller, url_prefix="/")
    viewer.register_blueprint(thanhcong, url_prefix="/")

    return viewer
