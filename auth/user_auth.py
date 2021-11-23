import base64

def user_auth(auth):
    auth = auth.split(sep=":")
    name = base64.b64decode(auth[0]).decode('UTF-8')
    password = base64.b64decode(auth[1]).decode('UTF-8')
    body = {
        "name": name,
        "password": password
    }
    return body