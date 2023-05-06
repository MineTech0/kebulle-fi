from datetime import date
from src import db


def vote_restaurant(restaurant_id):
    cur = db.connection.cursor()
    cur.execute('INSERT INTO votes (vote, created_at, restaurant_id) VALUES (%s, %s, %s)',
                (True, date.today(), restaurant_id))


def get_top5_restaurants():
    cur = db.connection.cursor()
    restaurants = []
    cur.execute("""
                SELECT r.id, r.name, c.name, COUNT(v.id) AS vote_count
                FROM restaurants r
                LEFT JOIN votes v ON r.id = v.restaurant_id
                LEFT JOIN cities c ON r.city_id = c.id
                WHERE v.vote = TRUE AND v.created_at >= %s AND v.created_at < %s
                GROUP BY r.id, c.name
                ORDER BY vote_count DESC
                LIMIT 5;
                """, (date.today().replace(day=1), date.today().replace(day=1, month=date.today().month + 1)))
    for i, row in enumerate(cur.fetchall()):
        restaurant = {
            'index': i + 1,
            'id': row[0],
            'name': row[1],
            'city': row[2],
            'votes': row[3],
        }
        restaurants.append(restaurant)
    return restaurants
