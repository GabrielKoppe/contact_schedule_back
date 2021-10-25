def set_json_to_query(json, user):

    query = f'''INSERT INTO contacts
    (id, name, email, zip_code, cellphone, address, address_number, creation_date, state, district, instagram, fav, user_id)
	VALUES ('{json['id']}', '{json['name']}', '{json['email']}', '{json['zip_code']}', '{json['cellphone']}', 
    '{json['address']}', '{json['address_number']}', '{json['creation_date']}', '{json['state']}', 
    '{json['district']}', '{json['instagram']}', 'false', '{user}') ;
    '''
    return query

def put_json_to_query(json, id, user):

    query = f'''UPDATE contacts
	SET name='{json['name']}', email='{json['email']}', zip_code='{json['zip_code']}', 
    cellphone='{json['cellphone']}', address='{json['address']}', address_number='{json['address_number']}', 
    state='{json['state']}', district='{json['district']}'
	WHERE id='{id}' AND user_id='{user}';'''

    return query

def delete_json_to_query(id, user):

    query = f'''DELETE FROM contacts
	WHERE id='{id}' AND user_id='{user}';'''

    return query