from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from ..services import account_service, transaction_service
from flask import make_response, jsonify


def account_user(view_function):
    @wraps(view_function)
    def decorator_function(*args, **kwargs):
        verify_jwt_in_request()
        user = get_jwt_identity()
        account = account_service.list_account_id(kwargs['id'])
        if account is None:
            return make_response(jsonify("Conta não encontrada"), 404)
        elif account.user_id == user:
            return view_function(*args, **kwargs)
        else:
            return make_response(jsonify("Está conta não pertence ao usuário logado"), 403)
    return decorator_function


def transaction_user(view_function):
    @wraps(view_function)
    def decorator_function(*args, **kwargs):
        verify_jwt_in_request()
        user = get_jwt_identity()
        transaction = transaction_service.list_transaction_id(kwargs['id'])
        if transaction is None:
            return make_response(jsonify("Transação não encontrada"), 404)
        else:
            account = account_service.list_account_id(transaction.account_id)
            if account.user_id == user:
                return view_function(*args, **kwargs)
            else:
                return make_response(jsonify("Está transação não pertence ao usuário logado"), 403)
    return decorator_function