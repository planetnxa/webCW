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
    revTxt = "another passion project. I thought it was 10/10. So did instagram, although I guess the likes didn't reflect that. None the less, this is definitely some of my best work"
    descTxt = "Someone called for elegance! Inspired by neutrals and minimalism, ABStudios is a passion project for a photography studio where the priority is capturing unfiltered beauty, and finding simplicity in the complex that is our world"
    portAlt="poster for AB studio. greyscale imag with elegant black woman with long body wave hair posing"
    portAlt1="brown and cream graphic with stylised letters AB, with the word STUDIOS in capitals"
    portAlt2="cream graphic with stylised letters AB, simple text saying STUDIOS, and a light skinned woman sitting on a chair with her feet out"
    portAlt3="AB logo visualised in black on white card, leaning on cream fabric"
    return render_template("port-temp.html", desc=descTxt, review=revTxt, imgPathMain=imgPathMain, imgPath1=imgPath1, imgPath2=imgPath2, imgPath3=imgPath3)


@app.route("/port-weLit")
def port_welit():
    imgPathMain="/static/weLit/zineCvr.jpg"
    imgPath1="/static/weLit/greenlogo.jpg"
    imgPath2="/static/weLit/metal.png" 
    imgPath3="/static/weLit/grillz.png"
    revTxt = "Another commission! I will not hold you this was waaay too good for me too not get booked. Nonetheless, this was such a fun project. Neutral, but fun"
    descTxt = "WeLit entertainment is a team of individuals dedicated to creating a good time for the urban community.As an extension of <<It's garra>>, WeLit work hard to provide quality events up North. They are for the people, by the people."
    portAlt = "poster for we lit entertainment. 5 black people posing in a picture, they look happy"
    portAlt1="green and grey graphic with stylised text saying weLit Entertainment, est 2023. Paragraphic text at the bottom explaining the concept behind the brand, as per project description"
    portAlt2="black background with metallic stylised text saying we Lit, with standard text on the word entertainment"
    portAlt3= "greyscale image of a closeup on a black person's mouth with metallic grilled teeth. In front says we Lit in flat bubble stylised text. The word entertainment is written in normal text"
    return render_template("port-temp.html", desc=descTxt, review=revTxt, imgPathMain=imgPathMain, imgPath1=imgPath1, imgPath2=imgPath2, imgPath3=imgPath3)


@app.route("/port-miakrylics")
def port_miaakrylics():
    imgPathMain="/static/mkVis/3b.jpg"
    imgPath3="/static/mkVis/1a.jpg"
    imgPath2="/static/mkVis/2-08.jpg" 
    imgPath1="/static/mkVis/1b.jpg"
    revTxt = "Can we take a moment to appreciate the colour scheme on this design? the orange gradients? the peaches? the perfect brown? Give Miakrylics her flowers!"
    descTxt = "This one is for my girlies! Miakrylics is your new favourite salon. based on Anywhere street, Cental Nondon, this is the perfect place to come and get your acrylics, manis, pedis and of course, more than enough tea, and gossip!"
    portAlt = "poster saying appointments out now for nail salon miakrylics. Includes cartoon graphic with hand holding crystal ball"
    portAlt1 = "logo for the brand MIAKRYLICS orange and yellow and red blur gradient with the letters MK in white at the front. brown text saying miakrylics overlays the white letters"
    portAlt2 = "3 phone mock-ups, with miakrylics assets on them."
    portAlt3 = "2 business cards with the Miakrylics logo and colour scheme printed on top. The other card has a pink-gloved hand on it."
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
        #find price of everything selected from string and pick up 4rm ther
        cmt = request.form[""]
        mailAdre = request.form["email"]
        name = request.form["name"]
        cmts = request.form["txt"]

        
        cost = db.Column(db.Float)


        s = models.Orders(cust_email=mailAdre,stock_bought=reqList,service_or_stock="service",date=datetime.datetime.utcnow())

        msg = "Hey"+name+"! \n Thank you for your enquiry, I really appreciate it.", 
        "In about two days I will get back to you about your enquiry. Until then," 
        "please pay the £30 deposit into my deposit via paypal.  \n\n\n I can't wait to work with you!"
        "\n\n Marie| NXADESIGNS"

    
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
