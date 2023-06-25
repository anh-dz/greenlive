from flask import Flask
web = Flask(__name__)

#dung <> de lam bien url
# còn có thể cài đặt biến trong url @web.route('/hello/<int:name>') float: path:
'''
@web.route('/hello/<name>')
def hello(name):
    return f"xin chao {name}"
'''

#add url rule
#web.add_url_rule('/','',hello)

web.run()