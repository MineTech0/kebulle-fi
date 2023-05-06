import os
import psycopg2

from urllib.parse import urlparse

dbc = urlparse(os.getenv("DATABASE_URL"))


connection = psycopg2.connect(
    dbname=dbc.path.lstrip('/'),
    user=dbc.username,
    password=dbc.password,
    host=dbc.hostname,
    port=dbc.port
)
connection.autocommit = True