from controller.contact_controller import set_localization

def set_json_to_query(json, user):

    query = f'''INSERT INTO contact
    (id, name, email, "zipCode", cellphone, address, "addressNumber", "creationDate", lat, "long", state, district, instagram, fav, user_id)
	VALUES ('{json['id']}', '{json['name']}', '{json['email']}', '{json['zipCode']}', '{json['cellphone']}', 
    '{json['address']}', '{json['addressNumber']}', '{json['creationDate']}', '{json['lat']}', '{json['long']}', '{json['state']}', 
    '{json['district']}', '{json['instagram']}', 'false', '{user}') ;
    '''
    return query

def put_json_to_query(json, id, user):

    json = set_localization(json)
    print(json)
    query = f'''UPDATE contact
	SET name='{json['name']}', email='{json['email']}', "zipCode"='{json['zipCode']}', 
    cellphone='{json['cellphone']}', address='{json['address']}', "addressNumber"='{json['addressNumber']}', 
    lat='{json['lat']}', "long"='{json['long']}', state='{json['state']}', district='{json['district']}'
	WHERE id='{id}' AND user_id='{user}';'''

    return query

def delete_json_to_query(id, user):

    query = f'''DELETE FROM contact
	WHERE id='{id}' AND user_id='{user}';'''

    return query