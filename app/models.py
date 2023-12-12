from app import db

#you can see the relationship tween order and what stock they have bought
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), index=True, unique=True)
    cust_email = db.Column(db.String(500), index=True, unique=True)
    address = db.Column(db.String(500), index=True, unique=True)
    stock_bought = db.Column(db.String(500), index=True, unique=True)
    service_or_stock = db.Column(db.String(500), index=True, unique=True)    
    date = db.Column(db.DateTime)
    cost = db.Column(db.Float)

#can be ordereed many times..draw the tables
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), index=True, unique=True)
    desc = db.Column(db.String(500), index=True, unique=True)
    ordered_by = db.Column(db.String(500), index=True, unique=True)
    count = db.Column(db.Integer)
    cost = db.Column(db.Float)

class Cust(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), index=True, unique=True)
    email = db.Column(db.String(500), index=True, unique=True)
    phone = db.Column(db.Integer)
    orders_list = db.Column(db.String(500), index=True, unique=True)


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), index=True, unique=True)
    requested_by = db.Column(db.String(500), index=True, unique=True)
    email_cust = db.Column(db.String(500), index=True, unique=True)
    cost = db.Column(db.Float)