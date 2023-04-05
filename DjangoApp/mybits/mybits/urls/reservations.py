from django.contrib import admin
from django.urls import path

import web.views as wb

urlpatterns_reservations = [
    path('Reservation/List', wb.reservations_list, 'Llista Reserves'),
    path('Reservation/Select', wb.select_reservation, name='Seleccionar Reserva'),
    path('Reservation/Book/<int:id_reservation>', wb.book, name='Reservar'),
    path('Reservation/Details/<int:id_reservation>', wb.reservation_details,name='Detalls Reserva')
]
