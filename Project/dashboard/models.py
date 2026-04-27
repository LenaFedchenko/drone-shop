from Project.db import DATA_BASE


class Delivery(DATA_BASE.Model):
    id = DATA_BASE.Column(DATA_BASE.Integer, primary_key=True)
    city = DATA_BASE.Column(DATA_BASE.String(50), nullable=True)
    streat = DATA_BASE.Column(DATA_BASE.String(50), nullable=True)
    house = DATA_BASE.Column(DATA_BASE.String(50), nullable=True)
    flat = DATA_BASE.Column(DATA_BASE.String(50), nullable=True)
    block = DATA_BASE.Column(DATA_BASE.String(50), nullable=True)
    is_selected = DATA_BASE.Column(DATA_BASE.Boolean, nullable=True, default=False)
    user_id = DATA_BASE.Column(DATA_BASE.Integer, DATA_BASE.ForeignKey('user.id'), nullable=False)