from src import db
from sqlalchemy import text

def getAll():
    result = db.connection.session.execute(text("SELECT * FROM regions"))
    regions = result.fetchall()
    return regions