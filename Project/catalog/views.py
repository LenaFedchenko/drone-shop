import flask
from Project.config_page import config_page
from .models import Product




@config_page("catalog.html")
def render_catalog():
    products = Product.query.all()
    return {
        "products": products
    }
    