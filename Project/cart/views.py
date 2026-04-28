import flask
from flask import request
from .utils import count_products_price
from catalog.models import Product
import dotenv, os, requests
from Project.loadenv import ENV_PATH

dotenv.load_dotenv(ENV_PATH)

def add_to_cart():
    product_id = request.json.get("product_id")
    id_list = flask.request.cookies.get("id_list")
    if not id_list:
        new_id_list = product_id
    else:
        new_id_list = id_list + "|" + product_id
    final_product_list = new_id_list.split(sep="|")
    product_count = final_product_list.count(product_id)
    response = flask.make_response(flask.jsonify({
        "status": "succes",
        "productsCount": product_count
    }))
    response.set_cookie(key="id_list", value=new_id_list)    
    return response



def render_cart():
    product_list = []
    cookies_id = flask.request.cookies.get("id_list")
    if cookies_id:
        id_list = cookies_id.split(sep="|")
        id_list_copy = id_list.copy()
        id_list_copy = set(id_list_copy)
        for id in id_list_copy:
            product = Product.query.get(id)
            product_list.append({
                "product" : product,
                "count" : id_list.count(id)
            })
    return flask.render_template("cart.html", products_list = product_list)


def count_sum():
    id = flask.request.cookies.get("id_list")
    sum = count_products_price(id)
    response = flask.make_response(flask.jsonify({
        "status": "succes",
        "totalPrice": sum
    }))
    print(response)

    return response

def delete_product_in_cart():
    product_id = request.json.get("product_id")
    id_list = flask.request.cookies.get("id_list").split(sep="|")
    id_list.remove(product_id)
    new_id_list = "|".join(id_list)
    finall_product_list = new_id_list.count(product_id)
    response = flask.make_response(flask.jsonify({
        "status" : "succes",
        "productsCount": finall_product_list
    }))
    if new_id_list:
        response.set_cookie(key="id_list", value=new_id_list)
    else:
        response.delete_cookie(key="id_list")
    return response


