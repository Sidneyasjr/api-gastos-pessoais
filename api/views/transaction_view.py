from flask import request, make_response, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from api import api
from ..entities import transaction
from ..schemas import transaction_schema
from ..services import transaction_service, account_service
from ..decorators import authorization_user


class TransactionList(Resource):
    @jwt_required
    def get(self):
        user = get_jwt_identity()
        transactions = transaction_service.list_transactions(user)
        ts = transaction_schema.TransactionSchema(many=True)
        return make_response(ts.jsonify(transactions), 200)

    @jwt_required
    def post(self):
        ts = transaction_schema.TransactionSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            description = request.json["description"]
            value_transaction = request.json["value_transaction"]
            type_transaction = request.json["type_transaction"]
            account = request.json["account_id"]
            if account_service.list_account_id(account) is None:
                return make_response("Conta não existe", 404)
            else:
                transaction_new = transaction.Transaction(name=name, description=description,
                                                          value_transaction=value_transaction,
                                                          type_transaction=type_transaction,
                                                          account=account)
                result = transaction_service.register_transaction(transaction_new)
                return make_response(ts.jsonify(result), 201)


class TransactionDetail(Resource):
    @authorization_user.transaction_user
    def get(self, id):
        transaction_id = transaction_service.list_transaction_id(id)
        ts = transaction_schema.TransactionSchema()
        return make_response(ts.jsonify(transaction_id), 200)

    @authorization_user.transaction_user
    def put(self, id):
        transaction_id = transaction_service.list_transaction_id(id)
        ts = transaction_schema.TransactionSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            description = request.json["description"]
            value_transaction = request.json["value_transaction"]
            type_transaction = request.json["type_transaction"]
            account = request.json["account_id"]
            if account_service.list_account_id(account) is None:
                return make_response("Conta não existe", 404)
            else:
                transaction_new = transaction.Transaction(name=name, description=description,
                                                          value_transaction=value_transaction,
                                                          type_transaction=type_transaction,
                                                          account=account)
                transaction_edit = transaction_service.edit_transaction(transaction_id, transaction_new)
                return make_response(ts.jsonify(transaction_edit), 200)

    @authorization_user.transaction_user
    def delete(self, id):
        transaction_id = transaction_service.list_transaction_id(id)
        transaction_service.remove_transaction(transaction_id)
        return make_response('', 204)



api.add_resource(TransactionList, '/transacoes')
api.add_resource(TransactionDetail, '/transacoes/<int:id>')
