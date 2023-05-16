from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *
import json
from django.core.exceptions import ValidationError





#Restaurants
def restaurant_list(request):
    all_restaurants = Restaurant.objects.all()
    return render(request, 'html/restaurants.html', {"restaurants" : all_restaurants})

def restaurant_detail(request, id_rest):
    one_restaurant = Restaurant.objects.get(pk=id_rest)
    restaurant_dict = model_to_dict(one_restaurant)
    context = {'restaurant': restaurant_dict}
    return render(request, 'html/restaurant.html', context)

#Localizations
def localization_list(request):
    all_localizations = Localization.objects.all()
    return render(request, 'html/localizations.html', {"localizations" : all_localizations})

def localization_detail(request, id_loc):
    one_localization = Localization.objects.get(pk=id_loc)
    return render(request, 'html/localization.html', {"localization" : one_localization})

#Clients
def client_list(request):
    all_clients = Client.objects.all()
    return render(request, 'html/clients.html', {"clients" : all_clients})

def client_detail(request, id_client):
    one_client = Client.objects.get(pk=id_client)
    return render(request, 'html/client.html', {"client" : one_client})

#Reservations
def reservation_list(request):
    all_reservations = Reservation.objects.all()
    return render(request, 'html/reservations.html', {"reservations" : all_reservations})

def reservation_detail(request, id_book):
    one_reservation = Reservation.objects.get(pk=id_book)
    return render(request, 'html/reservation.html', {"reservation" : one_reservation})

def create_order(request):
    if request.method == 'POST':
        description= request.POST.get('description')
    
        client_id = request.user.id
        
        order = Order()

        return redirect('order_detail', order_id=order.id)
    else:
        return render(request, 'html/create_order.html')

def booking_restaurant(request):
    if request.method == 'POST':
        date_order = request.POST.get('fecha')
        num_people = request.POST.get('people_num')
        id_client = request.user.id
        id_restaurant = request.POST.get('id_restaurant')

        # Obtener instancias de Client y Restaurant basadas en las claves foráneas
        client = get_object_or_404(Client, pk=1)
        restaurant = get_object_or_404(Restaurant, pk=1)

        booking = Reservation(date=date_order, people_num=num_people, id_client=client, id_restaurant=restaurant)
        booking.save()

        # Redirigir al usuario a la página de detalle de la nueva orden
        return redirect('order_detail', id_reservation=booking.id_reservation)
    else:
        return render(request, 'html/booking.html', {"restaurants": Restaurant.objects.all()})


#Orders
def order_list(request):
    all_orders = Order.objects.all()
    return render(request, 'html/orders_list.html', {"orders" : all_orders})

def order_detail(request, id_order):
    one_order = Order.objects.get(pk=id_order)
    return render(request, 'html/order_info.html', {"order" : one_order})



def restaurant_list(request):
    restaurants = Restaurant.objects.all() # obtiene todos los restaurantes de la base de datos
    context = {'restaurants': restaurants} # crea un diccionario de contexto que contiene la lista de restaurantes
    return render(request, 'html/restaurant_list.html', context) # renderiza la plantilla restaurant_list.html con el diccionario de contexto



@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@csrf_exempt
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
              messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    context = {}
    return render(request, 'registration/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    all_restaurants = Restaurant.objects.all()
    return render(request, 'html/home.html', {"restaurants" : all_restaurants})

@login_required(login_url='login')
def about(request):
    return render(request, 'html/about.html', None)