from datetime import date
from src import db
from src.modules import review as review_module


def get_restaurant_review_summary(restaurant_id):
    cur = db.connection.cursor()
    
    cur.execute("""
        SELECT 
            COALESCE(AVG(sauce_rating), 0) AS avg_sauce_rating, 
            COALESCE(AVG(meat_rating), 0) AS avg_meat_rating, 
            COALESCE(AVG(service_rating), 0) AS avg_service_rating, 
            COALESCE(AVG(price_rating), 0) AS avg_price_rating, 
            COALESCE(AVG(cleanliness_rating), 0) AS avg_cleanliness_rating, 
            COALESCE(AVG(sides_rating), 0) AS avg_sides_rating, 
            COALESCE(AVG(fries_rating), 0) AS avg_fries_rating 
        FROM reviews 
        WHERE restaurant_id = %s
    """, (restaurant_id,))
    
    review_summary = dict(zip(('avg_sauce_rating', 'avg_meat_rating', 'avg_service_rating', 'avg_price_rating', 'avg_cleanliness_rating', 'avg_sides_rating', 'avg_fries_rating'), cur.fetchone()))

    cur.close()
    print(review_summary)
    return review_summary

def insert_review(review):
    review['date'] = date.today()
    cur = db.connection.cursor()
    cur.execute(
        'INSERT INTO reviews (user_name, comment, date, sauce_rating, meat_rating, service_rating, price_rating, cleanliness_rating, sides_rating, fries_rating, restaurant_id, created_at, vegan_options) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)  RETURNING id;', (review['user_name'], review['comment'], review['date'], review['sauce_rating'], review['meat_rating'], review['service_rating'], review['price_rating'], review['cleanliness_rating'], review['sides_rating'], review['fries_rating'], review['restaurant_id'], date.today(), review['vegan_options']))
    rowId = cur.fetchone()[0]
    #updatae restaurant rating
    review_summary = review_module.get_restaurant_review_summary(review['restaurant_id'])
    rating = sum(review_summary.values()) / 7
    cur.execute("""
        UPDATE restaurants 
        SET rating = %s 
        WHERE id = %s
    """, (rating, review['restaurant_id']))
    cur.close()
    return rowId