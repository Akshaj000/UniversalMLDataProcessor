from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "headers": ["Content-Type"], "methods": ["GET", "POST"]}})

from api import routes


app.run(debug=True)
