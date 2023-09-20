# FOR TERMINAL when opening ubuntu: export FLASK_APP=flaskblog.py
                                     # export FLASK_DEBUG=1 
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd57424e55c6536c6f55d8a28c44849eb'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'mail.cloudwms.ro'
app.config['MAIL_PORT'] = 465
app.config['MAIl_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'test@cloudwms.ro'
app.config['MAIL_PASSWORD'] = 'hackerii123!'
mail = Mail(app)
mail.init_app(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.init_app(app)


from flaskblog import routes 


