import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__, instance_relative_config=True)
app.secret_key = os.getenv('SECRET_KEY')
csrf = CSRFProtect(app)

import src.routes