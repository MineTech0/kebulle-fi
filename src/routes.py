from flask import render_template, request, redirect, flash, url_for, session
from src.validators.new_restaurant_validator import new_restaurant_validator
from src.app import app
from src.modules import city, leaderboard, region, restaurant, review


@app.route('/')
def index():
    """Front page of the website.
    """

    return render_template('index.html', restaurant=restaurant.get_best_rated_restaurant(), leaderboard=leaderboard.get_top5_restaurants())


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/regions')
def regions():
    regions = region.get_all_with_cities()
    # remove empty regions
    regions = [region for region in regions if len(region['cities']) > 0]
    return render_template('regions.html', regions=regions)


@app.route('/restaurants', methods=['GET'])
def restaurants():
    city_name = request.args.get('city')
    restaurants_list = []
    if city_name:
        restaurants_list = restaurant.get_all_restaurants_by_city(city_name)
    else:
        restaurants_list = restaurant.get_all_restaurants()

    sort_by = request.args.get('sortBy')

    if sort_by and sort_by == 'rating':
        restaurants_list = sorted(
            restaurants_list, key=lambda k: k['rating'], reverse=True)
    elif sort_by and sort_by == 'name':
        restaurants_list = sorted(restaurants_list, key=lambda k: k['name'])

    return render_template('restaurants.html', restaurants=restaurants_list, city_name=city_name)


@app.route('/restaurants/create')
def create_restaurant():
    regions = region.get_all_with_cities()
    return render_template('create_restaurant.html', regions=regions)


@app.route('/restaurants', methods=['POST'])
def add_restaurant():
    name = request.form['name']
    address = request.form['address']
    city_id = request.form['city']
    if city_id == 'other':
        other_city_name = request.form['other-city']
        region_id = request.form['region']
        city_id = city.insert_city(other_city_name, region_id)
    restaurant.insert_restaurant(name, address, city_id)
    flash('Ravintola lisätty onnistuneesti!')
    return redirect('/restaurants')


@app.route('/restaurants/<int:id>/review/create')
def create_restaurant_review(id):
    return render_template('create_review.html', restaurant=restaurant.get_restaurant(id))


@app.route('/restaurants/<int:id>')
def show_restaurant(id):
    restaurant_data = restaurant.get_restaurant_with_reviews(id)
    review_summary = review.get_restaurant_review_summary(id)

    has_voted = session.get('has_voted')

    if review_summary:
        restaurant_data['rating'] = sum(review_summary.values()) / 7
    return render_template('restaurant.html', restaurant=restaurant_data, review_summary=review_summary, has_voted=has_voted)


@app.route('/restaurants/<int:restaurant_id>/review', methods=['POST'])
def add_review(restaurant_id):
    user_name = request.form['user_name']
    comment = request.form['comment']
    sauce_rating = request.form['sauce_rating']
    meat_rating = request.form['meat_rating']
    service_rating = request.form['service_rating']
    price_rating = request.form['price_rating']
    cleanliness_rating = request.form['cleanliness_rating']
    sides_rating = request.form['sides_rating']
    fries_rating = request.form['fries_rating']
    vegan_options = True if request.form.get('vegan_options') else False

    if not user_name or not comment:
        flash('Täytä nimi, kommentti ja päivämäärä.')
        return redirect(url_for('new_review'))

    new_review = {
        'user_name': user_name,
        'comment': comment,
        'sauce_rating': sauce_rating,
        'meat_rating': meat_rating,
        'service_rating': service_rating,
        'price_rating': price_rating,
        'cleanliness_rating': cleanliness_rating,
        'sides_rating': sides_rating,
        'fries_rating': fries_rating,
        'vegan_options': vegan_options,
        'restaurant_id': restaurant_id
    }

    review.insert_review(new_review)
    flash('Kiitos arvostelusta!')
    return redirect(url_for('show_restaurant', id=restaurant_id))


@app.route('/restaurants/<int:restaurant_id>/vote', methods=['POST'])
def vote(restaurant_id):
    if 'has_voted' in session and session.get('has_voted'):
        return redirect(url_for('show_restaurant', id=restaurant_id))
    # add session token for user to prevent multiple votes
    session['has_voted'] = True
    leaderboard.vote_restaurant(restaurant_id)
    return redirect(url_for('show_restaurant', id=restaurant_id))
