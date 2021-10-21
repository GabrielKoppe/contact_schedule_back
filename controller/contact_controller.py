from datetime import datetime
from geopy.geocoders import Nominatim
import json
import uuid

def new_contact(json_contact):
    json_contact = set_id(json_contact)
    json_contact = set_date(json_contact)
    json_contact = set_localization(json_contact)
    return json_contact

def set_id(data):
    data["id"] = uuid.uuid4() 
    return data

def set_date(data):
    data["creationDate"] = get_timestamp()
    return data

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def set_localization(data):
    try:
        geolocator = Nominatim(user_agent="ScheduleAPI")
        full_address = set_address(data)
        location = geolocator.geocode(full_address)
        data['lat'] = location.latitude
        data['long'] = location.longitude
        return data
    except:
        data['lat'] = ''
        data['long'] = ''
        return data

def set_address(data):
    full_address = f"{data['address']} {data['state']}"
    return full_address

def set_full_address(data):
    full_address = f"{data['address']}, {data['addressNumber']} - {data['district']} {data['state']} - {data['zipCode']}"
    return full_address