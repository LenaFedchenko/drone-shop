import flask
from Project.db import DATA_BASE
from catalog.models import Product
from sqlalchemy import select, desc

def render_home():
    new_products = products = Product.query.order_by(Product.id.desc()).limit(3).all()
    return flask.render_template("home.html", products=new_products)