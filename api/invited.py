from flask import request, Response, Blueprint, jsonify
import json

from controller.contact_controller import set_date
from data.data_tools import set_json_to_query_invited
from data.data_controller import execute_query

invited = Blueprint('invited', __name__)

#USER LOGIN
@invited.route('/invited', methods=['POST'])
def post_invited():
    try:
        body = json.loads(request.get_json())

        
        for invited in body:
            #400
            if not invited["nome"] or not invited["email"]:
               return jsonify({"error": "Campos não preenchidos"}), 400
            
        for invited in body:    

            invited = set_date(invited)

            query = set_json_to_query_invited(invited)

            #Execute SQL
            execute_query(query)

            print(query)
        
        #201
        return jsonify({"mensagem": "Presença confirmada!"}), 201

    except Exception as ex:
        #500
        return jsonify ({"error": str(ex)}), 500
