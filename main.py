from flask import *
from view import *
from control import *
import os

if __name__ == '__main__':
    viewer = Flask(__name__, template_folder="view/templates", static_folder="view/static")

    app = create_app(viewer)

if __name__ == '__main__':
    app.run(debug=True)