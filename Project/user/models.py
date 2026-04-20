from Project.db import DATA_BASE
from flask_login import UserMixin


class User(UserMixin, DATA_BASE.Model):
    id = DATA_BASE.Column(DATA_BASE.Integer, primary_key= True)
    first_name = DATA_BASE.Column(DATA_BASE.String(50), nullable= False)
    second_name = DATA_BASE.Column(DATA_BASE.String(50), nullable= True)
    last_name = DATA_BASE.Column(DATA_BASE.String(50), nullable= True)
    phone = DATA_BASE.Column(DATA_BASE.String(50), nullable= True)
    date_of_birth = DATA_BASE.Column(DATA_BASE.String(50), nullable= True)
    email = DATA_BASE.Column(DATA_BASE.String(50), nullable=False, unique=True)
    password = DATA_BASE.Column(DATA_BASE.String(35), nullable=False)
    isAdmin = DATA_BASE.Column(DATA_BASE.Boolean, default=False)