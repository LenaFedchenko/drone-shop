import flask
from catalog.models import Product
def render_home():
    new_products = Product.query.order_by(Product.id.desc()).limit(3).all()
    return flask.render_template("home.html", new_products=new_products)