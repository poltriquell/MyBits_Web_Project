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
from datetime import datetime





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


    return render(request, 'html/reservation.html', {"reservation" : one_reservation})


@login_required(login_url='login')
def order_detail(request, id_order):
    order = get_object_or_404(Order, pk=id_order)
    client = Client.objects.get(id_client=one_booking.id_client_id) 

    if client.username != request.user.username:
        return redirect('access_denied')
    return render(request, 'html/order_detail.html', {'order': order})


@login_required(login_url='login')
def create_order(request):
    if request.method == 'POST':
        user = request.user
        client = Client.objects.get(username=user.username)  # Find the client by their username

        id_restaurant = request.POST.get('restaurant')  # Get the selected restaurant ID correctly
        restaurant = get_object_or_404(Restaurant, pk=id_restaurant)  # Get the Restaurant instance based on the foreign key

        order = Order(date=datetime.now(), id_client=client, id_restaurant=restaurant)
        order.save()

        # Get the selected products from the form
        selected_products = request.POST.getlist('products')

        for product_id in selected_products:
            product = get_object_or_404(Product, pk=product_id)
            quantity = request.POST.get(f'quantity_{product_id}')
            order_item = OrderItem(order=order, id_producto=product, quantity=quantity)
            order_item.save()

        # Redirect the user to the order detail page
        return redirect('order_detail', id_order=order.id_order)
    else:
        return render(request, 'html/order.html', {"restaurants": Restaurant.objects.all()})



@login_required(login_url='login')
def booking_detail(request, id_reservation):
    one_booking = Reservation.objects.get(pk=id_reservation)
    client = Client.objects.get(id_client=one_booking.id_client_id) 
    if client.username != request.user.username:
        return redirect('access_denied')
    else:
        return render(request, 'html/booking_detail.html', {"booking" : one_booking})

@login_required(login_url='login')
def booking_restaurant(request):
    if request.method == 'POST':
        date_order = request.POST.get('fecha')
        num_people = request.POST.get('people_num')
        user = request.user
        client = Client.objects.get(username=user.username)  # Buscar el cliente por su nombre de usuario

        id_restaurant = request.POST.get('restaurant')  # Obtén el ID del restaurante seleccionado correctamente

        # Obtener la instancia de Restaurant basada en la clave foránea
        restaurant = get_object_or_404(Restaurant, pk=id_restaurant)
        booking = Reservation(date=date_order, people_num=num_people, id_client=client, id_restaurant=restaurant)
        booking.save()
        # Redirigir al usuario a la página de detalle de la nueva orden
        return redirect('book_detail', id_reservation=booking.id_reservation)
    else:
        return render(request, 'html/booking.html', {"restaurants": Restaurant.objects.all()})


    
@login_required(login_url='login')
def delete_booking(request, id_reservation):
    
    reservation = get_object_or_404(Reservation, pk=id_reservation)

    client = Client.objects.get(id_client=reservation.id_client_id) 
    # Verificar si el usuario autenticado es el propietario de la reserva
    if client.username != request.user.username:
        # Si el usuario no es el propietario, mostrar un mensaje de error o redirigir a una página de acceso denegado
        return redirect('access_denied')

    # Si el usuario es el propietario, eliminar la reserva
    reservation.delete()
    
    # Redirigir al usuario a alguna página de confirmación o a otra vista relevante
    return render(request, 'html/booking_deleted.html')     


@login_required(login_url='login')
def update_booking(request, id_reservation):
    if request.method == 'POST':
        reservation = get_object_or_404(Reservation, pk=id_reservation)
        client = Client.objects.get(id_client=reservation.id_client_id)
        if client.username != request.user.username:
            return redirect('access_denied')
        date_order = request.POST.get('fecha')
        num_people = request.POST.get('people_num')
        if not date_order:  # check if date_order is empty or None
            return render(request, 'html/booking_update.html', {"reservation": reservation, "error_message": "Date field is required."})
        reservation.date = date_order
        reservation.people_num = num_people
        reservation.save()
        return redirect('book_detail', id_reservation=reservation.id_reservation)
    else:
        reservation = get_object_or_404(Reservation, pk=id_reservation)
        return render(request, 'html/booking_update.html', {"reservation": reservation})



@login_required(login_url='login')
def user_bookings(request):
    
    user = request.user
    client = Client.objects.get(username=user.username)  # Obtén el cliente basado en el nombre de usuario
    if client.username != user.username:
            return redirect('access_denied')
    # Obtén todas las reservas del cliente actual
    bookings = Reservation.objects.filter(id_client=client)

    return render(request, 'html/user_bookings.html', {"bookings": bookings})



    
    

def access_denied(request):
    return render(request, 'html/access_denied.html')
    

#Orders
def order_list(request):
    all_orders = Order.objects.all()
    return render(request, 'html/orders_list.html', {"orders" : all_orders})




def restaurant_list(request):
    restaurants = Restaurant.objects.all() # obtiene todos los restaurantes de la base de datos
    context = {'restaurants': restaurants} # crea un diccionario de contexto que contiene la lista de restaurantes
    return render(request, 'html/restaurant_list.html', context) # renderiza la plantilla restaurant_list.html con el diccionario de contexto


@csrf_exempt
def register_page(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateUserForm()
    return render(request, 'registration/signup.html', {'form': form})


@csrf_exempt
def login_page(request):
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


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    all_restaurants = Restaurant.objects.all()
    return render(request, 'html/home.html', {"restaurants" : all_restaurants})

@login_required(login_url='login')
def about(request):
    return render(request, 'html/about.html', None)