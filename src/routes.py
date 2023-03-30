from flask import render_template
from src.app import app
from src.modules import region

@app.route('/')
def index():
    """Front page of the website.
    """
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/regions')
def regions():
    regions = region.getAll()
    return render_template('regions.html', regions=regions)

@app.route('/restaurants')
def restaurants():
    return render_template('restaurants.html')


@app.route('/restaurants/<int:restaurant_id>')
def restaurant(restaurant_id):
    return render_template('restaurant.html')
