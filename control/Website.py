from flask import Flask
import flask
from sqlalchemy.orm import Session
from sqlalchemy import select
from Databases import Links_point
from connect import engine
from Thong_ke_Db import qr_scanned
web_main_link = "localhost:5000/"
session = Session(bind=engine)
#Do a query searching for link 
def QR_query(link):
    return session.scalar(select(Links_point).where(Links_point.address == link))
#Checking if this link is inside of database
def QR_link_check(link):
    return QR_query(link) is not None
#delete link after done
def QR_link_remove(link):
    session.delete(QR_query(link))
    session.commit()
web = Flask(__name__)
@web.route("/qr/<name>/")
def func(name: str):
    link = f"{web_main_link}qr/{name}"
    if QR_link_check(link):
        QR_link_remove(link)
        qr_scanned(session, 1)
        return  flask.render_template("point.html", status = "Valid")
    else:
        return flask.render_template("point.html", status = "Invalid")
web.run()
