import os
import django
import sqlite3

# Configurar la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mybits.settings')
django.setup()

from django.contrib.auth.models import User
from web.models import *



def populate_restaurants():
    restaurantes = [
        {
            'name': 'La brasería de Adrián Sanz',
            'phone': '600000000',
            'email': 'reservar@braseria.blv',
            'website': 'www.braseriasanz.com',
            'longitude': 41.6897,
            'latitude': 0.178438
        },
        {
            'name': 'Restaurante vegano de Pol Triquell',
            'phone': '611111111',
            'email': 'reservas@veganotriquell.lbb',
            'website': 'www.restaurantepol.lbb',
            'longitude': 41.5203322,
            'latitude': 0.8684098
        },
        
        
    ]
    
    for restaurante in restaurantes:
        Restaurant.objects.create(
            name=restaurante['name'],
            phone=restaurante['phone'],
            email=restaurante['email'],
            website=restaurante['website'],
            longitude=restaurante['longitude'],
            latitude=restaurante['latitude']
        )


def populate_users():
    users = [
        {
           'username': 'CodeinaUser',
           'password': 'hola12345'
        },
        {
           'username': 'MarioBrosUser',
           'password': 'hola12345'
        },
        {
           'username': 'ElQuiqueUser',
           'password': 'hola12345'
        }
    ]
    
    for user in users:
        User.objects.create_user(
            username=user['username'],
            password=user['password']
        )


def populate_super_user():
    User.objects.create_superuser(
        username='enric',
        password='hola12345',
        email='enric@admin.com'
    )  


def populate_clients():
    clients = [
        {
            'username': 'CodeinaUser',
            'name': 'Mr. Codina',
            'DNI_NIE': '44555666P',
            'address': 'Calle Rural',
            'phone': '622222222',
            'email': 'codina@gmail.com',
            'card_number': '0000111122223333'
        },
        {
            'username': 'MarioBrosUser',
            'name': 'Lord Mario',
            'DNI_NIE': '77888999P',
            'address': 'Calle Afueras',
            'phone': '633333333',
            'email': 'mario@gmail.com',
            'card_number': '4444555566667777'
        },
        {
            'username': 'ElQuiqueUser',
            'name': 'Don Enric',
            'DNI_NIE': '11222333P',
            'address': 'Calle 11S',
            'phone': '644444444',
            'email': 'enric@gmail.com',
            'card_number': '8888999900001111'
        }
    ]
    
    for client in clients:
        Client.objects.create(
            username=client['username'],
            name=client['name'],
            DNI_NIE=client['DNI_NIE'],
            address=client['address'],
            phone=client['phone'],
            email=client['email'],
            card_number=client['card_number']
        )


def populate_products():
    products = [
        {
            'restaurant': 'La brasería de Adrián Sanz',
            'name': 'T-bone steak',
            'price': '25.99',
            'description': 'Juicy grilled T-bone steak with seasoned fries'
        },
        {
            'restaurant': 'La brasería de Adrián Sanz',
            'name': 'Seafood Paella',
            'price': '18.99',
            'description': 'Traditional Spanish paella with a variety of fresh seafood'
        },
        {
            'restaurant': 'Restaurante vegano de Pol Triquell',
            'name': 'Vegan Burger',
            'price': '12.99',
            'description': 'Plant-based burger with vegan cheese and avocado'
        },
        {
            'restaurant': 'Restaurante vegano de Pol Triquell',
            'name': 'Quinoa Salad',
            'price': '9.99',
            'description': 'Healthy salad made with quinoa, mixed greens, and fresh vegetables'
        }
    ]

    for product in products:
        restaurant = Restaurant.objects.get(name=product['restaurant'])
        Product.objects.create(
            id_restaurant=restaurant,
            name=product['name'],
            price=product['price'],
            description=product['description']
        )


if __name__ == '__main__':
    populate_restaurants()
    populate_users()
    populate_super_user()
    populate_clients()
    populate_products()

