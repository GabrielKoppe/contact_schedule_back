from flask import request, Response, Blueprint, jsonify, send_file
import json
import pandas as pd

from controller.contact_controller import set_date
from data.data_tools import set_json_to_query_invited
from data.data_controller import execute_query, execute_read_query

from communicate.body import invite_email

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

            email = invite_email(invited['email'].lower(), invited['nome'])

            if email: 
                at_email = f'''UPDATE public.invited
                SET email_invited = true
                WHERE email = '{invited['email']}';
                '''
                execute_query(at_email)
        
        #201
        return jsonify({"mensagem": "Obrigado! Vamos enviar um e-mail confirmando sua presença."}), 201

    except Exception as ex:
        #500
        return jsonify ({"error": str(ex)}), 500

#USER LOGIN
@invited.route('/data', methods=['GET'])
def get_data():
    try:
        #Set query SQL
        query = f'''SELECT nome, email, email_invited, TO_CHAR(creation_date, 'YYYY-MM-DD HH:MI') as creation_date FROM public.invited'''

        #Execute SQL
        data_list = execute_read_query(query)

        pd.DataFrame(data_list).to_excel('CasamentoLista.xlsx')

        #200
        return send_file("CasamentoLista.xlsx", as_attachment=True)
    
    except Exception as ex:
        #500
        return jsonify ({"error": str(ex)}), 500