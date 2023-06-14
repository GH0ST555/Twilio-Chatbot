from flask import Flask

from flask_login import LoginManager
# from flask_admin import Admin
from flask_mail import Mail
import logging

app = Flask(__name__)
app.config.from_object('config')
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'arjun.krishnan0033@gmail.com'
# app.config['MAIL_PASSWORD'] = 'gipdqkxoemurrytz'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)


# logging.basicConfig(filename='record.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'



# admin = Admin(app,template_mode='bootstrap4')

from app import views
