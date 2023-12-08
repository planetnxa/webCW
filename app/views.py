from app import app
from flask import render_template, request, session
from sqlalchemy import func
# import db for context purposes, and place databse work in the actual application functions

# initialise these at -1 so when we start we can differentiate between no input, and zero values
"""
how to ensure emails and ting
layout

"""


@app.route("/")  # the url for us to work with
def index():
    return render_template("index.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/port-abstudio")
def port_abstudio():
    imgPathMain="/static/abfinals/bwCvr.jpg"
    imgPath1="/static/abfinals/LOGO.png"
    imgPath2="/static/abfinals/beigeimg.jpg" 
    imgPath3="/static/abfinals/crdmock.png"
    revTxt = "lil review vieeeww"
    descTxt = "a nice snazzy example text"
    return render_template("port-temp.html", desc=descTxt, review=revTxt, imgPathMain=imgPathMain, imgPath1=imgPath1, imgPath2=imgPath2, imgPath3=imgPath3)


@app.route("/port-weLit")
def port_welit():
    imgPathMain="/static/weLit/zineCvr.jpg"
    imgPath1="/static/weLit/greenlogo.jpg"
    imgPath2="/static/weLit/metal.png" 
    imgPath3="/static/weLit/grillz.png"
    revTxt = "Another commission! I will not hold you this was waaay too good for me too not get booked. Nonetheless, this was such a fun project. Neutral, but fun"
    descTxt = "a nice snazzy example text"
    return render_template("port-temp.html", desc=descTxt, review=revTxt, imgPathMain=imgPathMain, imgPath1=imgPath1, imgPath2=imgPath2, imgPath3=imgPath3)


@app.route("/port-miakrylics")
def port_miaakrylics():
    imgPathMain="/static/mkVis/3b.jpg"
    imgPath1="/static/mkVis/1a.jpg"
    imgPath2="/static/mkVis/2-08.jpg" 
    imgPath3="/static/mkVis/1b.jpg"
    revTxt = "lil review vieeeww"
    descTxt = "a nice snazzy example text"
    return render_template("port-temp.html", desc=descTxt, review=revTxt, imgPathMain=imgPathMain, imgPath1=imgPath1, imgPath2=imgPath2, imgPath3=imgPath3)


@app.route("/book-me")
def book():
    return render_template("book.html")


@app.route("/book-conf")
def book_conf():
    return render_template("book-confirmation.html")


@app.route("/shop")
def shop():
    return render_template("shop.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/admin-view")
def admin_orders():
    return render_template("admin-view.html")

    # intialise the other balances and values etc
