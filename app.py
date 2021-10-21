from flask import Flask, Response, Blueprint
from flask_cors import CORS

from api.contact import contact

# Create the application instance
app = Flask(__name__)
CORS(app)

# Create a URL route in our application for "/"
@app.route('/')
def hello_world():
    return 'This is the Schedule API!'

#Add APIs
app.register_blueprint(contact)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)