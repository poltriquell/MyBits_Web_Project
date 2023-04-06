from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Restaurant, Localization, Meal, Client, Reservation, Order, Menu

def home(request):
    return render(request, 'web/home.html', None)

def restaurant_list(request):
    all_restaurants = Restaurant.objects.all()
    return render(request, 'web/restaurant.html', {"restaurants" : all_restaurants})

def restaurant_detail(request, pk):
    pk_str = str(pk)
    return HttpResponse("Hello, world. You're at restaurant " + pk_str + " description.")

def localization_list(request):
    return HttpResponse("Hello, world. You're at localization list.")

def localization_detail(request, pk):
    pk_str = str(pk)
    return HttpResponse("Hello, world. You're at restaurant " + pk_str + " localization detail.")

def meal_list(request):
    return HttpResponse("Hello, world. You're at meal list.")

def meal_detail(request, pk):
    pk_str = str(pk)
    return HttpResponse("Hello, world. You're at restaurant " + pk_str + " meal detail.")

def client_list(request):
    return HttpResponse("Hello, world. You're at client list.")

def client_detail(request, pk):
    pk_str = str(pk)
    return HttpResponse("Hello, world. You're at client detail " + pk_str + " description.")

def reservation_list(request):
    return HttpResponse("Hello, world. You're at reservation list.")

def reservation_detail(request, pk):
    pk_str = str(pk)
    return HttpResponse("Hello, world. You're at restaurant " + pk_str + " reservation detail.")

def order_list(request):
    return HttpResponse("Hello, world. You're at order list.")

def order_detail(request, pk):
    pk_str = str(pk)
    return HttpResponse("Hello, world. You're at restaurant " + pk_str + " order detail.")

def menu_list(request):
    return HttpResponse("Hello, world. You're at menu list.")

def menu_detail(request, pk):
    pk_str = str(pk)
    return HttpResponse("Hello, world. You're at restaurant " + pk_str + "menu detail.")