from datetime import date
from src import db


def insert_restaurant(name, address, city_id):
    cur = db.connection.cursor()
    created_at = date.today()
    updated_at = date.today()
    cur.execute('INSERT INTO restaurants (name, address, city_id, rating, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)',
                (name, address, city_id, 0, created_at, updated_at))
    db.connection.commit()


def get_all_restaurants():
    cur = db.connection.cursor()
    cur.execute('SELECT r.id, r.name, r.address, c.name, re.name, r.rating FROM restaurants r JOIN cities c ON r.city_id=c.id JOIN regions re ON c.region_id=re.id ORDER BY r.rating DESC')
    restaurants = []
    for row in cur.fetchall():
        restaurant = {
            'id': row[0],
            'name': row[1],
            'address': row[2],
            'city': row[3],
            'region': row[4],
            'rating': row[5]
        }
        restaurants.append(restaurant)
    return restaurants


def get_all_restaurants_by_city(city_name):
    cur = db.connection.cursor()
    cur.execute('SELECT r.id, r.name, r.address, c.name, re.name, r.rating FROM restaurants r JOIN cities c ON r.city_id=c.id JOIN regions re ON c.region_id=re.id WHERE c.name = %s ORDER BY r.rating DESC', (city_name,))
    restaurants = []
    for row in cur.fetchall():
        restaurant = {
            'id': row[0],
            'name': row[1],
            'address': row[2],
            'city': row[3],
            'region': row[4],
            'rating': row[5]
        }
        restaurants.append(restaurant)
    return restaurants


def get_restaurant(restaurant_id):
    cur = db.connection.cursor()
    cur.execute('SELECT r.id, r.name, r.address, c.name, re.name, r.rating FROM restaurants r JOIN cities c ON r.city_id=c.id JOIN regions re ON c.region_id=re.id WHERE r.id = %s', (restaurant_id,))
    row = cur.fetchone()
    if row is None:
        return None
    restaurant = {
        'id': row[0],
        'name': row[1],
        'address': row[2],
        'city': row[3],
        'region': row[4],
        'rating': row[5],
        'reviews': []
    }
    return restaurant


def get_restaurant_with_reviews(restaurant_id):
    cur = db.connection.cursor()

    # Query the restaurant information
    cur.execute("""
        SELECT r.id, r.name, r.address, c.name AS city, rg.name AS region, r.rating
        FROM restaurants r
        JOIN cities c ON r.city_id = c.id
        JOIN regions rg ON c.region_id = rg.id
        WHERE r.id = %s
    """, (restaurant_id,))
    row = cur.fetchone()

    if row is None:
        cur.close()
        return None

    restaurant = {
        'id': row[0],
        'name': row[1],
        'address': row[2],
        'city': row[3],
        'region': row[4],
        'rating': row[5],
        'reviews': []
    }

    # Query the reviews for the restaurant
    cur.execute("""
        SELECT rv.id, rv.user_name, rv.comment, rv.date, rv.sauce_rating, rv.meat_rating,
               rv.service_rating, rv.price_rating, rv.cleanliness_rating, rv.sides_rating, rv.fries_rating,
               rv.vegan_options
        FROM reviews rv
        WHERE rv.restaurant_id = %s
        ORDER BY rv.date DESC;
    """, (restaurant_id,))
    rows = cur.fetchall()

    for row in rows:
        review = {
            'id': row[0],
            'user_name': row[1],
            'comment': row[2],
            'date': row[3],
            'sauce_rating': row[4],
            'meat_rating': row[5],
            'service_rating': row[6],
            'price_rating': row[7],
            'cleanliness_rating': row[8],
            'sides_rating': row[9],
            'fries_rating': row[10],
            'vegan_options': row[11]
        }
        restaurant['reviews'].append(review)

    cur.close()

    print(restaurant)

    return restaurant


def get_best_rated_restaurant():
    cur = db.connection.cursor()
    cur.execute('SELECT r.id, r.name, r.address, c.name, re.name, r.rating FROM restaurants r JOIN cities c ON r.city_id=c.id JOIN regions re ON c.region_id=re.id ORDER BY r.rating DESC LIMIT 1')
    row = cur.fetchone()
    if row is None:
        return None
    restaurant = {
        'id': row[0],
        'name': row[1],
        'address': row[2],
        'city': row[3],
        'region': row[4],
        'rating': row[5]
    }
    return restaurant
