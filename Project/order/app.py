import flask

order = flask.Blueprint(
    name='order',
    import_name='order',
    template_folder='templates',
    static_folder='static',
    static_url_path='/order/static'
)