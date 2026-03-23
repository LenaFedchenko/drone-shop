import flask
from Project.db import DATA_BASE
from .models import Order

def render_order():
    if flask.request.method == "POST":
        first_name = flask.request.form["first_name"]
        second_name = flask.request.form["second_name"]
        surname = flask.request.form["surname"]
        phone = flask.request.form["phone"]
        email = flask.request.form["email"]
        message = flask.request.form["message"]
        order = Order(
            first_name,
            second_name,
            surname,
            phone,
            email,
            message
        )
        DATA_BASE.session.add(order)
        DATA_BASE.session.commit()
    return flask.render_template('order.html')

