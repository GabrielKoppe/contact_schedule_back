from flask import Flask, request, Response, Blueprint, jsonify
import json
import uuid

from data.data_controller import execute_read_query, execute_query
from auth.passwords import compara_senha, cod_senha
from auth.create_jwt import create_jwt

user = Blueprint('user', __name__)

#CREATE NEW USER
@user.route('/user', methods=['POST'])
def add_new():
    try:
        body = request.get_json()
        
        body["id"] = uuid.uuid4()
        body["password"] = cod_senha(body["password"]).decode('utf8')
        body["name"] = body["name"].lower()

        query = f'''INSERT INTO "user" (id, name, password) VALUES ('{body['id']}', '{body['name']}', '{body['password']}');'''
        print(query)

        execute_query(query)

        return Response (json.dumps("Success!"), mimetype="application/json", status=200)
    except Exception as ex:
        print(str(ex))
        return jsonify ({"error": str(ex)}), 500


#USER LOGIN
@user.route('/login', methods=['POST'])
def get_login():
    try:
        body = request.get_json()

        user = execute_read_query(f'''SELECT * FROM "user" Where name = '{body["name"].lower()}';''')[0]

        if user['password'] == -1:
            return jsonify({"error": "Usuario não encontrado"}), 400

        if not compara_senha(user['password'], body.get('password')):
            return jsonify({"error": "Senha invalida"}), 401
        else:
            payload = create_jwt(user['id'], user['name'])
            return jsonify(payload), 200
    except Exception as ex:
        return jsonify ({"error": str(ex)}), 500
