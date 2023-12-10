from app import app
from flask import render_template, request, session,redirect,url_for
from datetime import datetime
from sqlalchemy import func
import smtplib
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

#################
@app.route("/shop-crzn1")
def shop_crzn1():
    shopName="CORAZON HOODIE"
    shopDesc="123"
    shopPrice="223"
    # just pass in the object lool, for name price and count
    #if item count is 0
    
    return render_template("shop-temp.html", shopDesc=shopDesc, shopName=shopName, shopPrice=shopPrice, shopImg0=imgPath, shopImg1=imgPath1, shopImg2=imgPath2, shopImg3=imgPath3)

@app.route("/shop-crzn2")
def shop_crzn2():
   
   
    shopName="CORAZON HOODIE"
    shopDesc="123"
    shopPrice="223"
    # just pass in the object lool, for name price and count
    #if item count is 0
    
    return render_template("shop-temp.html", shopDesc=shopDesc, shopName=shopName, shopPrice=shopPrice, shopImg0=imgPath, shopImg1=imgPath1, shopImg2=imgPath2, shopImg3=imgPath3)

@app.route("/shop-crzn3")
def shop_crzn3():
    
    shopName="CORAZON HOODIE"
    shopDesc="123"
    shopPrice="223"
    # just pass in the object lool, for name price and count
    #if item count is 0
    
    return render_template("shop-temp.html", shopDesc=shopDesc, shopName=shopName, shopPrice=shopPrice, shopImg0=imgPath, shopImg1=imgPath1, shopImg3=imgPath2, shopImg2=imgPath3)


@app.route("/shop-crzn4")
def shop_crzn4():
    
    shopName="CORAZON HOODIE"
    shopDesc="123"
    shopPrice="223"
    # just pass in the object lool, for name price and count
    #if item count is 0
    
    return render_template("shop-temp.html", shopDesc=shopDesc, shopName=shopName, shopPrice=shopPrice, shopImg0=imgPath, shopImg1=imgPath1, shopImg3=imgPath2, shopImg2=imgPath3)

@app.route("/shop-brwn1")
def shop_brwn1():
    
    shopName="CORAZON HOODIE"
    shopDesc="123"
    shopPrice="223"
    # just pass in the object lool, for name price and count
    #if item count is 0
    
    return render_template("shop-temp.html", shopDesc=shopDesc, shopName=shopName, shopPrice=shopPrice, shopImg0=imgPath, shopImg1=imgPath1, shopImg2=imgPath2, shopImg3=imgPath3)

@app.route("/shop-brwn2")
def shop_brwn2():
    
    shopName="CORAZON HOODIE"
    shopDesc="123"
    shopPrice="223"
    # just pass in the object lool, for name price and count
    #if item count is 0
    
    return render_template("shop-temp.html", shopDesc=shopDesc, shopName=shopName, shopPrice=shopPrice, shopImg0=imgPath, shopImg1=imgPath1, shopImg3=imgPath2, shopImg2=imgPath3)
0

@app.route("/book-me", methods=["POST","GET"])
def book():
    if request.method == "POST":
        #if we are collecting data
        date = datetime.datetime.utcnow()
        reqList = request.form.getlist("req")
        cmt = request.form[""]
        mailAdre = request.form["email"]
        name = request.form["name"]
        cmts = request.form["txt"]

        msg = "Hey"+name+"! \n Thank you for your enquiry, I really appreciate it.", 
        "In about two days I will get back to you about your enquiry. Until then," 
        "please pay the £30 deposit into my deposit via paypal.  \n\n\n I can't wait to work with you!"
        "\n\n Marie| NXADESIGNS"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("nxadesigns1@gmail.com", "N395dkeX.")
        server.sendmail("nxadesigns1@gmail.com",mailAdre,message)

        #make database entry
        #input it,, make session

       # db.session.add(p)
        # db.session.commit()

    else:

        return render_template("book.html")


@app.route("/book-conf")
def book_conf():
    return render_template("book-confirmation.html")


@app.route("/shop")
def shop():
    return render_template("shop.html")
############################################################
@app.route("/admin", methods={"POST", "GET"})
def admin():
    if request.method == "POST":
        password = request.form["pw"]
        if password != "123":
            adminMsg = "incorrect password try again"
            return render_template("admin.html",pwMessage=adminMsg)
        else:
            session["admin"] = password
            return render_template("admin-view.html")
    else:
        return render_template("admin.html",pwMessage="")


@app.route("/admin-view", methods={"POST", "GET"})
def admin_orders():
    if request.method == "POST":
        session.pop("admin",None)
        return redirect(url_for("admin_orders"))
    else:
        if "admin" in session:
            return render_template("admin-view.html")
        else:
            return render_template("admin.html",pwMessage="")
    # intialise the other balances and values etc
