from api import db
import enum


class TypeEnum(enum.Enum):
    entry = 1
    exit = 2


class Transaction(db.Model):
    __tablename__ = "transaction"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    value_transaction = db.Column(db.Float, nullable=False)
    type_transaction = db.Column(db.Enum(TypeEnum), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))
    account = db.relationship("Account", backref=db.backref("transactions", lazy="dynamic"))