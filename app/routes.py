from flask import Blueprint, render_template, jsonify
from app.models import Product
from faker import Faker
import random

main = Blueprint('main', __name__)
fake = Faker()

# Sample product categories and adjectives for more realistic product names
product_categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Sports & Outdoors']
adjectives = ['Sleek', 'Stylish', 'Modern', 'Classic', 'Comfortable', 'Functional', 'Durable', 'Premium']

@main.route('/')
def index():
    # Generate fake product data for demonstration
    fake_products = generate_fake_products()

    # Uncomment the line below if you want to add fake data to the database
    # add_fake_products_to_database(fake_products)

    return render_template('index.html', products=fake_products)

@main.route('/api/products')
def get_products():
    # Generate fake product data for the API endpoint
    fake_products = generate_fake_products()
    return jsonify(fake_products)

def generate_fake_products():
    fake_products = []

    for _ in range(100):
        category = random.choice(product_categories)
        adjective = random.choice(adjectives)
        product_name = f'{adjective} {category}'

        # Generate random price within a range appropriate for each category
        if category == 'Electronics':
            price = round(random.uniform(100, 1000), 2)
        elif category == 'Clothing':
            price = round(random.uniform(10, 100), 2)
        elif category == 'Home & Kitchen':
            price = round(random.uniform(20, 500), 2)
        elif category == 'Books':
            price = round(random.uniform(5, 50), 2)
        else:
            price = round(random.uniform(10, 200), 2)

        fake_product = {
            'name': product_name,
            'price': price
        }
        fake_products.append(fake_product)

    return fake_products

# Uncomment the function below if you want to add fake data to the database
# from app import db
# def add_fake_products_to_database(fake_products):
#     for fake_product in fake_products:
#         product = Product(name=fake_product['name'], price=fake_product['price'])
#         db.session.add(product)
#     db.session.commit()
