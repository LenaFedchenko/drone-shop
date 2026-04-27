import flask, flask_login
from user.models import User
from order.models import Order
from Project.db import DATA_BASE



def render_contact():
    if not flask_login.current_user.is_authenticated:
        return flask.redirect("/login")
    
    user = User.query.filter_by(id=flask_login.current_user.id).first()
    if flask.request.method == "POST":
        first_name = flask.request.form["first_name"]
        last_name = flask.request.form["last_name"]
        second_name = flask.request.form["second_name"]
        date = flask.request.form["date"]
        phone = flask.request.form["phone"]
        email = flask.request.form["email"]
        user.first_name = first_name
        user.last_name = last_name
        user.second_name = second_name
        user.date_of_birth = date
        user.phone = phone
        user.email = email
        DATA_BASE.session.commit()


    return flask.render_template("contact-page.html", user=user)

def render_orders():
    if not flask_login.current_user.is_authenticated:
        return flask.redirect("/login")
    user_id = flask_login.current_user.id
    orders_list = Order.query.filter_by(id=user_id).all()
    

    return flask.render_template("my-orders.html", orders=orders_list)

def render_delivery():
    if not flask_login.current_user.is_authenticated:
        return flask.redirect("/login")
    user_id = flask_login.current_user.id
    user = User.query.filter_by(id=user_id).first()
