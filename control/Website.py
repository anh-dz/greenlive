from flask import Flask
from control import running
import flask
from sqlalchemy.orm import Session
from sqlalchemy import select
from Databases import Links_point
from connect import engine
session = Session(bind=engine)
#Do a query searching for link 
def QR_query(link):
    statement = select(Links_point).where(Links_point.address == link)
    result = session.scalar(statement)
    return result
#Checking if this link is inside of database
def QR_link_check(link):
    result = QR_query(link)
    return result is not None
#delete link after done
def QR_link_remove(link):
    result = QR_query(link)
    session.delete(result)
    session.commit()
web = Flask(__name__)
@web.route("/qr/<name>/")
def func(name):
    link = running + f"qr/{name}"
    if QR_link_check(link):
        return  flask.render_template("point.html", status = "Valid")
    else:
        return flask.render_template("point.html", status = "Invalid")
web.run()