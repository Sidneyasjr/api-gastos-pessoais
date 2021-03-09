from api import db
from ..models import account_model


def register_account(account):
    account_db = account_model.Account(name=account.name, description=account.description, balance=account.balance,
                                       user_id=account.user)
    db.session.add(account_db)
    db.session.commit()
    return account_db


def list_account(user):
    accounts = account_model.Account.query.filter_by(user_id=user).all()
    return accounts


def list_account_id(id):
    account = account_model.Account.query.filter_by(id=id).first()
    return account


def remove_account(account):
    db.session.delete(account)
    db.session.commit()


def edit_account(account, account_new):
    account.name = account_new.name
    account.description = account_new.description
    account.balance = account_new.balance
    db.session.commit()
    return account


def alter_balance_account(account_id, transaction, type_operation, value_old=None):
    # 1: Register
    # 2: Edition
    # 3: Removal
    account = list_account_id(account_id)
    if type_operation == 1:
        # Edition
        if transaction.type_transaction == "1":
            account.balance += transaction.value_transaction
        else:
            account.balance -= transaction.value_transaction
    elif type_operation == 2:
        # Edition
        if transaction.type_transaction == "1":
            account.balance -= value_old
            account.balance += transaction.value_transaction
        else:
            account.balance += value_old
            account.balance -= transaction.value_transaction
    else:
        # Removal
        if transaction.type_transaction.value == 1:
            account.balance -= transaction.value_transaction
        else:
            account.balance += transaction.value_transaction
    db.session.commit()
