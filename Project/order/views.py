import flask, requests, flask_login
from Project.db import DATA_BASE
from .models import Order
from user.models import User
import os
from catalog.models import Product
from cart.utils import count_products_price


def render_order():
    if not flask_login.current_user.is_authenticated:
        return flask.redirect("/login")
    user_id = flask_login.current_user.id
    user = User.query.filter_by(id=user_id).first()
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
    
    return flask.render_template('order.html', products_list=product_list)

def get_warehouses(city_name: str):
    TOKEN = os.environ["NOVA_POST_TOKEN"]
    delivery_type = flask.request.args.get('type')
    
    payload = {
        "api_key": TOKEN,
        "modelName": "Address",
        "calledMethod": "getWarehouses",
        "methodProperties": {
            "CityName": city_name
        }
    }
    response = requests.post(
        "https://api.novaposhta.ua/v2.0/json/",
        json=payload
    )
    result = response.json()
    warehouses = []
    for data in result["data"]:
        # print(data["TypeOfWarehouse"], data["Description"])
        if data["TypeOfWarehouse"] == "841339c7-591a-42e2-8233-7a0a00f0ed6f" and delivery_type == "warehouse":
            warehouses.append(data["Description"])
        elif data["TypeOfWarehouse"] == "f9316480-5f2d-425d-bc2c-ac7cd29decf0" and delivery_type == "parcel_machine":
            warehouses.append(data["Description"])
        elif data["TypeOfWarehouse"] == "6f8c7162-4b72-4b0a-88e5-906948c6a92f" and delivery_type == "expres_delivery":
            warehouses.append(data["Description"])
        elif data["TypeOfWarehouse"] == "9a68df70-0267-42a8-bb5c-37f427e36ee4" and delivery_type == "courier":
            warehouses.append(data["Description"])    
    response = flask.make_response(flask.jsonify({
        "warehouses" : warehouses
    }))
    return response

def pay():
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
    if flask.request.method == "POST":
        first_name = flask.request.form["first_name"]
        second_name = flask.request.form["second_name"]
        surname = flask.request.form["surname"]
        phone = flask.request.form["telephone"]
        email = flask.request.form["email"]
        message = flask.request.form["message"]
        payment = flask.request.form["payment"]
        user_id = flask_login.current_user.id
        order = Order(
            first_name= first_name,
            second_name= second_name,
            surname= surname,
            phone= phone,
            email= email,
            message= message,
            pay_method = payment,
            warehouse = "",
            user_id=user_id
        )
        for product in product_list:
            order.products.append(product["product"])
        DATA_BASE.session.add(order)
        DATA_BASE.session.commit()
    raw_id_list = flask.request.cookies.get("id_list") 
    sum = count_products_price(raw_id_list=raw_id_list)

    if payment == "card":
        TOKEN = os.environ["MONOBANK_TOKEN"]
        payload = {
            "amount": sum * 100,
            "ccy": 980,
            "redirectUrl": "http://127.0.0.1:8000"
        }
        headers = {
            "X-Token": TOKEN
        }
        response = requests.post(
            "https://api.monobank.ua/api/merchant/invoice/create",
            json=payload,
            headers=headers
            )
        request = response.json()
        pay_url = request["pageUrl"]
        return flask.redirect(pay_url)
    
    return flask.redirect("/")
