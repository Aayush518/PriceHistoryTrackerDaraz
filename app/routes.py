# app/routes.py

from flask import Blueprint, render_template
from app.models import Product
from faker import Faker

main = Blueprint('main', __name__)
fake = Faker()

@main.route('/')
def index():
    # Generate fake product data for demonstration
    fake_products = [
        {'name': fake.word(), 'price': fake.random_number(2)},
        {'name': fake.word(), 'price': fake.random_number(2)},
        {'name': fake.word(), 'price': fake.random_number(2)},
        # Add more fake product entries as needed
    ]

    # Uncomment the line below if you want to add fake data to the database
    add_fake_products_to_database(fake_products)

    return render_template('index.html', products=fake_products)

# Uncomment the function below if you want to add fake data to the database
from app import db
def add_fake_products_to_database(fake_products):
    for fake_product in fake_products:
        product = Product(name=fake_product['name'], price=fake_product['price'])
        db.session.add(product)
    db.session.commit()
