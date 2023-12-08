from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import views

#initialising the Flask object and then importing views so we can see the html web visuals
# the flask object is called app