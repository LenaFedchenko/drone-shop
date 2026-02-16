from catalog.models import Product

def count_products_price(raw_id_list):
    sum = 0
    if raw_id_list:
        id_list = raw_id_list.split(sep="|")
    else:
        id_list = []
    for item in id_list:
        product = Product.query.get(item).price
        sum += product
    return sum