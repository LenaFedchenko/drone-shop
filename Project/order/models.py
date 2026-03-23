from Project.db import DATA_BASE


class Order(DATA_BASE.Model):
    id = DATA_BASE.Column(DATA_BASE.Integer, primary_key=True)
    first_name = DATA_BASE.Column(DATA_BASE.String(50), nullable=True)
    second_name = DATA_BASE.Column(DATA_BASE.String(50), nullable=True)
    surname = DATA_BASE.Column(DATA_BASE.String(50), nullable=True)
    phone = DATA_BASE.Column(DATA_BASE.Integer, nullable=True)
    email = DATA_BASE.Column(DATA_BASE.String(50), nullable=True)
    message = DATA_BASE.Column(DATA_BASE.String(1000), nullable=True)
    warehouse = DATA_BASE.Column(DATA_BASE.String(50), nullable=True)
    pay_method = DATA_BASE.Column(DATA_BASE.String(50), nullable=True)
    products = DATA_BASE.Column(DATA_BASE.String, nullable=True)