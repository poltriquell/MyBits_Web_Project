from django.contrib import admin
from django.urls import path

import web.views as wb

urlpatterns_dishes = [
     path('Dishes/List', wb.dishes_list, name='Llista_Plats'),
]