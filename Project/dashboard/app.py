import flask

dashboard = flask.Blueprint(
    name='dashboard',
    import_name='dashboard',
    template_folder='templates',
    static_folder='static',
    static_url_path='/dashboard/static'
)