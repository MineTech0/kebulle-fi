from src import db


def insert_city(name, region_id):
    cur = db.connection.cursor()
    cur.execute(
        'INSERT INTO cities (name, region_id) VALUES (%s, %s)  RETURNING id;', (name, region_id))
    rowId = cur.fetchone()[0]
    return rowId

