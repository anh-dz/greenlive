from flask import Flask

def create_app():
    app = Flask(__name__)

    from .home import homepage
    from .reg import register

    app.register_blueprint(homepage, url_prefix="/")
    app.register_blueprint(register, url_prefix="/")

    return app
