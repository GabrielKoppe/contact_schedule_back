from flask import current_app
import datetime
import jwt

def create_jwt(id, nome):
    payload = {
        "id": id,
        "name": nome
    }
    token = jwt.encode(payload, current_app.config['SECRET_KEY'])
    payload['token'] = token
    return payload