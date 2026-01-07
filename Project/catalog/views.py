import flask
from Project.config_page import config_page
from .models import Product
from flask import request




def render_catalog():
    page = request.args.get("page", 1, type= int)
    pagination = Product.query.paginate(page=page, per_page=1)
    return flask.render_template("catalog.html", products=pagination.items, pagination= pagination)