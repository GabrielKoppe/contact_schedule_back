from datetime import datetime
import uuid

def new_contact(json_contact):
    json_contact = set_id(json_contact)
    json_contact = set_date(json_contact)
    return json_contact

def set_id(data):
    data["id"] = uuid.uuid4() 
    return data

def set_date(data):
    data["creation_date"] = get_timestamp()
    return data

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def set_full_address(data):
    full_address = f"{data['address']}, {data['address_number']} - {data['district']} {data['state']} - {data['zip_code']}"
    return full_address