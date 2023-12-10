from app import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cust_email = db.Column(db.String(500), index=True, unique=True)
    address = db.Column(db.String(500), index=True, unique=True)
    stock_bought = db.Column(db.String(500), index=True, unique=True)
    service_or_stock = db.Column(db.String(500), index=True, unique=True)    
    date = db.Column(db.DateTime)
    cost = db.Column(db.Float)

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
    orders_list = db.Column(db.String(500), index=True, unique=True)
    count = db.Column(db.Integer)
    cost = db.Column(db.Float)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), index=True, unique=True)
    requested_by = db.Column(db.String(500), index=True, unique=True)
    email_cust = db.Column(db.String(500), index=True, unique=True)
    cost = db.Column(db.Float)