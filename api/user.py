from flask import request, Response, Blueprint, jsonify
import json
import uuid

from data.data_controller import execute_read_query, execute_query
from auth.passwords import compara_senha, cod_senha
from auth.create_jwt import create_jwt
from auth.user_auth import user_auth

user = Blueprint('user', __name__)

#CREATE NEW USER
@user.route('/user', methods=['POST'])
def add_new():
    try:
        auth = request.headers.get('Authorization')
        body = user_auth(auth)

        #Set id
        body["id"] = uuid.uuid4()

        #Set Name
        if body["name"] != '':
            body["name"] = body["name"].lower()
        else:
            return jsonify({"error": "User was not passed"}), 400

        #Set Password
        if body["password"] != '':
            body["password"] = cod_senha(body["password"]).decode('utf8')
        else:
            return jsonify({"error": "Password was not passed"}), 400

        try:
            #400 User create
            execute_read_query(f'''SELECT name FROM users Where name = '{body["name"].lower()}';''')[0]
            return jsonify({"error": "User has already been created"}), 400
        except:
            query = f'''INSERT INTO users (id, name, password) VALUES ('{body['id']}', '{body['name']}', '{body['password']}');'''

            execute_query(query)

            return Response (status=201)
    except Exception as ex:
        return jsonify ({"error": str(ex)}), 500


#USER LOGIN
@user.route('/login', methods=['POST'])
def get_login():
    try:
        auth = request.headers.get('Authorization')
        body = user_auth(auth)

        #Set Name
        if body["name"] == '': return jsonify({"error": "User was not passed"}), 400

        #Set Password
        if body["password"] == '': return jsonify({"error": "Password was not passed"}), 400

        try:
            user = execute_read_query(f'''SELECT * FROM users Where name = '{body["name"].lower()}';''')[0]
        except:
            return jsonify({"error": "Usuario não encontrado"}), 400

        if not compara_senha(user['password'], body.get('password')):
            return jsonify({"error": "Senha invalida"}), 401
        else:
            payload = create_jwt(user['id'], user['name'])
            return jsonify(payload), 200
    except Exception as ex:
        return jsonify ({"error": str(ex)}), 500
