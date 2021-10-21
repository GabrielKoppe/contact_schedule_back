from flask import Flask, request, Response, Blueprint, jsonify
import json

from data.data_controller import execute_read_query, execute_query
from controller.contact_controller import new_contact
from data.data_tools import set_json_to_query, put_json_to_query, delete_json_to_query

contact = Blueprint('contact', __name__)

#CREATE   /contact/fav/
@contact.route('/contact', methods=['POST'])
def add_new():
    
    #Json request
    body = request.get_json()
    print(body)
    try:
        #Contact new ajust
        body = new_contact(body)
        
        #400
        if not body["name"]:
            return Response (status=400)

        #SQL Ajust
        query = set_json_to_query(body)
        
        #Execute SQL
        execute_query(query)

        #201
        return Response (status=201)

    except Exception as ex:
        #500
        return jsonify (str(ex)), 500

#READ
@contact.route('/contact')
def get():
    try:
        #get http query
        order_type = request.args.get('order')
        
        #type of filter
        if order_type == 'asc':
            order = "ORDER by name asc"
        elif order_type == 'date':
            order = '''ORDER by "creationDate"'''
        elif order_type == 'like':
            order = '''ORDER by fav desc'''
        else:
            order = ''

        #Set query SQL
        query = f'''SELECT id, name, fav FROM contact {order}'''
        print(query)
        #Execute SQL
        contact_list = execute_read_query(query)

        #200
        return jsonify(contact_list), 200
    
    except Exception as ex:
        #500
        return jsonify (str(ex)), 500

@contact.route('/contact/<id_busca>')
def get_by_id(id_busca):
    try:
        query = "SELECT * FROM contact WHERE id='{}'".format(id_busca)

        #Execute SQL
        contact_list = execute_read_query(query)

        #200
        return jsonify(contact_list[0]), 200

    except Exception as ex:
        #500
        return jsonify (str(ex)), 500

#UPDATE
@contact.route('/contact/<id_busca>', methods=['PUT'])
def update_(id_busca):
    
    #Json request
    body = request.get_json()

    try:
        print(body)
        #Set query SQL
        query = put_json_to_query(body, id_busca)
        print(query)
        #Execute SQL
        execute_query(query)

        return Response (status=201)
    except Exception as ex:
        return jsonify (str(ex)), 500

#DELETE
@contact.route('/contact/<id_busca>', methods=['DELETE'])
def delete_by_id(id_busca):
    try:
        
        #Set query SQL
        query = delete_json_to_query(id_busca)

        #Execute SQL
        execute_query(query)

        return Response (status=201)
    except Exception as ex:
        return jsonify (str(ex)), 500

#CHANGE FAV 
@contact.route('/contact/fav/<id_busca>', methods=['PUT'])
def post_fav(id_busca):
    try:
        #get http query
        fav = request.args.get('fav')

        #SQL Ajust
        query = "UPDATE contact SET fav={} WHERE id='{}'".format(fav, id_busca)
        print(query)
        #Execute SQL
        execute_query(query)

        #201
        return Response (status=201)

    except Exception as ex:
        #500
        return jsonify (str(ex)), 500