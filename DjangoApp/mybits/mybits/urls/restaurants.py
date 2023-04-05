from django.contrib import admin
from django.urls import path

import web.views as wb

urlpatterns_restaurants = [
    path('Restaurant/List', wb.restaurants_list, 'Llista_Restaurants'),
    path('Restaurant/Restaurant/Add/<int:id>', wb.add_restaurant, name='Afegir_Restaurant'),
    path('Restaurant/Restaurant/Delete/<int:id>', wb.delete_restaurant, name='Esborrar_Restaurant'),
    path('Restaurant/Restaurant/Edit/<int:id>', wb.edit_restaurant, name='Editar_Restaurant'),
    path('Restaurant/Restaurant/Description/<int:id>', wb.restaurant_description, name='Descripció_Restaurant')
]
