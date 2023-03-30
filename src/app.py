import os

from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.secret_key = os.getenv('SECRET_KEY')

import src.routes