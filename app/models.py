from app import db

#association table!
link_orders = db.Table("item_init",
db.Column("order_id",db.Integer,db.ForeignKey("order.id")),
db.Column("item_id",db.Integer,db.ForeignKey("item.id"))

)

#you can see the relationship tween order and what stock they have bought
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), index=True)
    cust_email = db.Column(db.String(500), index=True, )
    address = db.Column(db.String(500), index=True, )
    stock_bought = db.relationship("Item",secondary=link_orders,backref="order_deets")
    date = db.Column(db.DateTime)
    cost = db.Column(db.Float)

#can be ordereed many times..draw the tables
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), index=True, )
    ordered_by = db.Column(db.String(500), index=True, )
    count = db.Column(db.Integer)
    cost = db.Column(db.Float)
    service_or_stock = db.Column(db.String(500), index=True)    

class Cust(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), index=True, )
    email = db.Column(db.String(500), index=True, )
    phone = db.Column(db.Integer)
    orders_list = db.Column(db.String(500), index=True, )
