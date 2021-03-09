from ..models import user_model
from api import db


def register_user(user):
    user_db = user_model.User(name=user.name, email=user.email, password=user.password)
    user_db.gen_password()
    db.session.add(user_db)
    db.session.commit()
    return user_db


def list_user_email(email):
    return user_model.User.query.filter_by(email=email).first()


def list_user_id(id):
    return user_model.User.query.filter_by(id=id).first()