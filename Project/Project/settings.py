import flask, os, dotenv
from .loadenv import ENV_PATH
from flask_mail import Mail

dotenv.load_dotenv(ENV_PATH)

project = flask.Flask(
    import_name= 'Project',
    template_folder= 'templates',
    static_folder= 'static',
    static_url_path= '/static/',
    instance_path= os.path.abspath(os.path.join(__file__, '..', 'instance'))
)

project.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
project.config["MAIL_SERVER"] = 'smtp.gmail.com'
project.config["MAIL_PORT"] = 587
project.config["MAIL_USE_TLS"] = True
project.config["MAIL_USE_SSL"] = False
project.config["MAIL_USERNAME"] = os.environ["MAIL"]
project.config["MAIL_PASSWORD"] = os.environ["PASSWORD"]
project.config["MAIL_DEFAULT_SENDER"] = os.environ["MAIL"]

mail = Mail(project)