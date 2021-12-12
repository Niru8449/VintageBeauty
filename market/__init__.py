from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'd7ff6eb552e7a1f2ee01111b'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

# if __name__ == "__main__":
#     app.run(debug = True)
login_manager=LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from market import routes


