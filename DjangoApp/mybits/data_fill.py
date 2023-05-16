import os
import django

# Configurar la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mybits.settings')

django.setup()
from django.contrib.auth.models import User
from web.models import *

import sqlite3

def clear_database():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Obtener una lista de tablas en la base de datos
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Eliminar los datos de todas las tablas
    for table in tables:
        table_name = table[0]
        cursor.execute(f"DELETE FROM {table_name};")

    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

    print("Contenido de la base de datos eliminado exitosamente.")

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
            'longitude': 41.5203322 ,
            'latitude': 0.8684098 
        }
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
           'username' : 'Codeina',
           'password' : 'hola12345'
        },
        {
           'username' : 'MarioBros',
           'password' : 'hola12345'
        },
        {
           'username' : 'ElQuique',
           'password' : 'hola12345'
        }
    ]
    
    for user in users:
        User.objects.create_user(
            username=user['username'],
            password=user['password']
        )
        

def populate_clients():
    clients = [
        {
            'username' : 'Codeina',
            'name': 'Mr. Codina',
            'DNI_NIE' : '44555666P',
            'address' : 'Calle Rural',
            'phone' : '622222222',
            'email' : 'codina@gmail.com',
            'card_number' : '0000111122223333'
        },
        {
            'username' : 'MarioBros', 
            'name': 'Lord Mario',
            'DNI_NIE' : '77888999P',
            'address' : 'Calle Afueras',
            'phone' : '633333333',
            'email' : 'mario@gmail.com', 
            'card_number' : '4444555566667777'
        },
        {
            'username' : 'ElQuique', 
            'name': 'Don Enric', 
            'DNI_NIE' : '11222333P', 
            'address' : 'Calle 11S', 
            'phone' : '644444444', 
            'email' : 'enric@gmail.com', 
            'card_number' : '8888999900001111'
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
        
if __name__ == '__main__':
    populate_restaurants()
    populate_users()
    populate_clients()