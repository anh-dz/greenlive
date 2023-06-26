from flask import Flask
from view import *
from control import *

if __name__ == '__main__':
    viewer = Flask(__name__, template_folder="view/templates", static_folder="view/static")

    app = create_app(viewer)

    app.run(debug=True)
