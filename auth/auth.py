from functools import wraps
from flask import request, jsonify, current_app
import jwt

def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None

        if 'authorization' in request.headers:
            token = request.headers['authorization']

        if not token: 
            return jsonify({"error": "Sem permissão para acessar essa rota."}), 401
        
        if not "Bearer" in token:
            return jsonify({"error": "token invalido"}), 403

        try:
            token_pure = token.replace("Bearer ", "")
            decoded = jwt.decode(token_pure, current_app.config['SECRET_KEY'], algorithms=['HS256', ])

            current_id = decoded['id']
            current_name = decoded['name']
        except:
            return jsonify({"error": "O token é inválido"}), 403

        return f(current_name=current_name, current_id=current_id, *args, **kwargs)
    return wrapper
