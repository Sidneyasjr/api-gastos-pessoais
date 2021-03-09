from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config')
jwt = JWTManager(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)
mi = Migrate(app, db)

api = Api(app)

from .models import account_model, transaction_model, user_model
from .views import account_view, transaction_view, user_view, login_view, refresh_token_view