from django.contrib import admin
from django.urls import path

import web.views as wb

urlpatterns_restaurants = [
    path('Restaurant/List', wb.llista_restaurants, 'Llista Restaurants'),
    
]
