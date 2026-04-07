from Project.db import DATA_BASE

product_order = DATA_BASE.Table(
    "product_order",
    DATA_BASE.Column('product_id', DATA_BASE.Integer, DATA_BASE.ForeignKey('product.id'), primary_key=True),
    DATA_BASE.Column('order_id', DATA_BASE.Integer, DATA_BASE.ForeignKey('order.id'), primary_key=True)
)