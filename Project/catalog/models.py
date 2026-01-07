from Project.db import DATA_BASE

class Product(DATA_BASE.Model):
    id = DATA_BASE.Column(DATA_BASE.Integer, primary_key= True)
    name = DATA_BASE.Column(DATA_BASE.String(100), nullable=False)
    price = DATA_BASE.Column(DATA_BASE.Integer, nullable=False)
    old_price = DATA_BASE.Column(DATA_BASE.Integer, nullable=False)
    image_url = DATA_BASE.Column(DATA_BASE.String(100), nullable=False)
    category = DATA_BASE.Column(DATA_BASE.String(50), nullable=False)
    description = DATA_BASE.Column(DATA_BASE.String(500), nullable=False)