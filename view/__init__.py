from flask import Flask
from .home import homepage
from .reg import register
from .log import login

def create_app(viewer):
    viewer.register_blueprint(homepage, url_prefix="/")
    viewer.register_blueprint(register, url_prefix="/")
    viewer.register_blueprint(login, url_prefix="/")

    return viewer
