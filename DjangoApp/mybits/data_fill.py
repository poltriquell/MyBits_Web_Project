import os
import django

# Configurar la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mybits.settings')

django.setup()
from web.models import Restaurant

def populate_restaurants():
    restaurantes = [
        {
            'name': 'Restaurante 1',
            'phone': '123456789',
            'email': 'restaurante1@example.com',
            'website': 'www.restaurante1.com',
            'longitude': 41.6001,
            'latitude': 0.6227
        },
        {
            'name': 'Restaurante 2',
            'phone': '987654321',
            'email': 'restaurante2@example.com',
            'website': 'www.restaurante2.com',
            'longitude': 41.6020,
            'latitude': 0.6228
        },
        {
            'name': 'Restaurante 3',
            'phone': '456123789',
            'email': 'restaurante3@example.com',
            'website': 'www.restaurante3.com',
            'longitude': 42.6003,
            'latitude': 0.6509
        },
        
        # Agrega aquí los demás restaurantes
        {
            'name': 'Restaurante 12',
            'phone': '753951456',
            'email': 'restaurante12@example.com',
            'website': 'www.restaurante12.com',
            'longitude': 42.6014,
            'latitude': 0.6337
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




if __name__ == '__main__':
    populate_restaurants()
