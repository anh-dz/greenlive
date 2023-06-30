from flask import *
from view import *
from control import *
#import os
global Login_manager
viewer = Flask(__name__, template_folder="view/templates", static_folder="view/static")

    #viewer.config.update(SECRET_KEY=os.urandom(24))
viewer.config.update(SECRET_KEY='SuperSecret')
viewer.config.from_object(__name__)

app = create_app(viewer)
Login_manager = login_manager_create(app, Session(engine))
    

if __name__ == '__main__':
    app.run(debug=True)