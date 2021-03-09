from ..models import transaction_model, account_model
from api import db
from ..services.account_service import alter_balance_account


def register_transaction(transaction):
    transaction_bd = transaction_model.Transaction(name=transaction.name, description=transaction.description,
                                                   value_transaction=transaction.value_transaction,
                                                   type_transaction=transaction.type_transaction,
                                                   account_id=transaction.account)
    db.session.add(transaction_bd)
    db.session.commit()
    alter_balance_account(transaction.account, transaction, 1)
    return transaction_bd


def list_transactions(user):
    transactions = transaction_model.Transaction.query.join(account_model.Account).filter_by(user_id=user).all()
    return transactions


def list_transaction_id(id):
    transaction_id = transaction_model.Transaction.query.filter_by(id=id).first()
    return transaction_id


def edit_transaction(transaction_id, transaction_new):
    value_old = transaction_id.value_transaction
    transaction_id.name = transaction_new.name
    transaction_id.description = transaction_new.description
    transaction_id.value_transaction = transaction_new.value_transaction
    transaction_id.type_transaction = transaction_new.type_transaction
    transaction_id.account = transaction_new.account
    db.session.commit()
    alter_balance_account(transaction_new.account, transaction_new, 2, value_old)
    return transaction_id


def remove_transaction(transaction):
    db.session.delete(transaction)
    db.session.commit()
    alter_balance_account(transaction.account_id, transaction, 3)
