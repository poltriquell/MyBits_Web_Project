from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView
from .models import Restaurant, Localization, Client, Reservation, Order, Menu

def home(request):
    all_restaurants = Restaurant.objects.all()
    return render(request, 'web/home.html', {"restaurants" : all_restaurants})

#Restaurants
def restaurant_list(request):
    all_restaurants = Restaurant.objects.all()
    return render(request, 'web/restaurants.html', {"restaurants" : all_restaurants})

def restaurant_detail(request, id_rest):
    one_restaurant = Restaurant.objects.get(pk=id_rest)
    return render(request, 'web/restaurant.html', {"restaurant" : one_restaurant})

#Localizations
def localization_list(request):
    all_localizations = Localization.objects.all()
    return render(request, 'web/localizations.html', {"localizations" : all_localizations})

def localization_detail(request, id_loc):
    one_localization = Localization.objects.get(pk=id_loc)
    return render(request, 'web/localization.html', {"localization" : one_localization})

#Clients
def client_list(request):
    all_clients = Client.objects.all()
    return render(request, 'web/clients.html', {"clients" : all_clients})

def client_detail(request, id_client):
    one_client = Client.objects.get(pk=id_client)
    return render(request, 'web/client.html', {"client" : one_client})

#Reservations
def reservation_list(request):
    all_reservations = Reservation.objects.all()
    return render(request, 'web/reservations.html', {"reservations" : all_reservations})   

def reservation_detail(request, id_book):
    one_reservation = Reservation.objects.get(pk=id_book)
    return render(request, 'web/reservation.html', {"reservation" : one_reservation})

#Orders
def order_list(request):
    all_orders = Order.objects.all()
    return render(request, 'web/orders.html', {"orders" : all_orders})  

def order_detail(request, id_order):
    one_order = Order.objects.get(pk=id_order)
    return render(request, 'web/order.html', {"order" : one_order})

#Menus
def menu_list(request):
    all_menus = Menu.objects.all()
    return render(request, 'web/menus.html', {"menus" : all_menus})  

def menu_detail(request, id_rest):
    one_menu = Menu.objects.get(pk=id_rest)
    return render(request, 'web/menu.html', {"menus" : one_menu})

#Login
def login(request):
    return render(request, 'web/login.html', None)

def register(request):
    return render(request, 'web/register.html', None)

#About Us
def about(request):
    return render(request, 'web/about.html', None)