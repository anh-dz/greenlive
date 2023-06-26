from flask import Flask
from .home import *
from .reg import *
from .log import *
from .au1 import  *
from .au2 import *

def create_app(viewer):
    viewer.register_blueprint(homepage, url_prefix="/")
    viewer.register_blueprint(register, url_prefix="/")
    viewer.register_blueprint(login, url_prefix="/")
    viewer.register_blueprint(afteruser1, url_prefix="/")
    viewer.register_blueprint(afteruser2, url_prefix="/")

    return viewer
