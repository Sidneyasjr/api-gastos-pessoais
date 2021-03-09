from api import api
from flask_restful import Resource
from ..schemas import login_schema
from flask import request, make_response, jsonify
from ..services.user_service import list_user_email
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta


class LoginList(Resource):
    def post(self):
        ls = login_schema.LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        email = request.json["email"]
        password = request.json["password"]
        user_bd = list_user_email(email)
        if user_bd and user_bd.see_password(password):
            access_token = create_access_token(
                identity=user_bd.id,
                expires_delta=timedelta(seconds=200)
            )
            refresh_token = create_refresh_token(identity=user_bd.id)
            return make_response(jsonify({
                'access_token': access_token,
                'refresh_token': refresh_token,
                'message': 'Login Realizado com sucesso'
            }), 200)
        return make_response(jsonify({'message': 'Credenciais inválidas'}), 401)


api.add_resource(LoginList, '/login')