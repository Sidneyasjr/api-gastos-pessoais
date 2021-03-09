from flask_restful import Resource
from ..schemas import account_schema
from flask import request, make_response, jsonify
from ..entities import account
from ..services import account_service, user_service
from api import api
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..decorators import authorization_user


class AccountList(Resource):
    @jwt_required
    def get(self):
        user = get_jwt_identity()
        accounts = account_service.list_account(user)
        acs = account_schema.AccountSchema(many=True)
        return make_response(acs.jsonify(accounts), 200)

    @jwt_required
    def post(self):
        acs = account_schema.AccountSchema()
        validate = acs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            description = request.json["description"]
            balance = request.json["balance"]
            user = get_jwt_identity()
            account_new = account.Account(name=name, description=description, balance=balance, user=user)
            result = account_service.register_account(account_new)
            return make_response(acs.jsonify(result), 201)


class AccountDetail(Resource):
    @authorization_user.account_user
    def get(self, id):
        account_id = account_service.list_account_id(id)
        acs = account_schema.AccountSchema()
        return make_response(acs.jsonify(account_id), 200)

    @authorization_user.account_user
    def put(self, id):
        account_id = account_service.list_account_id(id)
        acs = account_schema.AccountSchema()
        validate = acs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            description = request.json["description"]
            balance = request.json["balance"]
            user = get_jwt_identity()
            account_new = account.Account(name=name, description=description, balance=balance, user=user)
            result = account_service.edit_account(account_id, account_new)
            return make_response(acs.jsonify(result), 201)

    @authorization_user.account_user
    def delete(self, id):
        account_id = account_service.list_account_id(id)
        account_service.remove_account(account_id)
        return make_response('', 204)



api.add_resource(AccountList, '/contas')
api.add_resource(AccountDetail, '/contas/<int:id>')

