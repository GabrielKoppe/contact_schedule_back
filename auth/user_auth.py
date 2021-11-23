import base64

def user_auth(auth):
    print(auth)
    if "Basic" in auth:
        auth = auth.replace("Basic ","")
    auth = base64.b64decode(auth).decode('UTF-8')
    auth = auth.split(sep=":")
    name = auth[0]
    password = auth[1]
    body = {
        "name": name,
        "password": password
    }
    return body