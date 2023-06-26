from flask import Flask

def create_app():
    app = Flask(__name__)

    from .home import homepage
    from .reg import register
    from .login import login_bp

    app.register_blueprint(homepage, url_prefix="/")
    app.register_blueprint(register, url_prefix="/")
    app.register_blueprint(login_bp, url_prefix="/")

    return app
