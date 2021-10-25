from flask import Flask, Response, Blueprint
from flask_cors import CORS
from dotenv import load_dotenv
import os

from api.contact import contact
from api.user import user

load_dotenv()

# Create the application instance
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
CORS(app)

# Create a URL route in our application for "/"
@app.route('/')
def hello_world():
    return 'This is the Schedule API!'

#Add APIs
app.register_blueprint(contact)
app.register_blueprint(user)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)