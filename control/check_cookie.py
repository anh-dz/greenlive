from flask import Flask
from flask import render_template, make_response, request
#def makecookie()
app = Flask(__name__, template_folder="./")
@app.route('/cookie')
def cookies():
    resp = make_response(render_template('sam.html'))
    resp.set_cookie('login', 'true')
    resp.set_cookie('username', 'katori')
    resp.set_cookie('password', 'conga123')
    return resp
@app.route('/')
def get_cookie():
    result = request.cookies.get('username')
    print(result)
    if result == 'false':
        return "Chua dang nhap ma lam gi day?"
    else:
        return "Ok di tiep di"
app.run()