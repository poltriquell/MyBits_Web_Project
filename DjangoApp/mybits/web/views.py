from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the home.")

def sign_in(request):
    return HttpResponse("Hello, world. You're at the authentication.")

def profile(request):
    return HttpResponse("Hello, world. You're at the profile.")

def edit_profile(request):
    return HttpResponse("Hello, world. You're at the editing menu.")

#Restaurants
def restaurants_list(request):
    return HttpResponse("Hello, world. You're at the restaurants list.")

def add_restaurant(request):
    return HttpResponse("Hello, world. You're at the add menu.")
    
def delete_restaurant(request):
    return HttpResponse("Hello, world. You're at the delete menu.")
    
def edit_restaurant(request):
    return HttpResponse("Hello, world. You're at the edition menu.")
    
def restaurant_description(request):
    return HttpResponse("Hello, world. You're at the restaurant's description.")
 
 #Reservations
def reservations_list(request):
    return HttpResponse("Reservations list")

def select_reservation(request):
    return HttpResponse("Select reservation")

def book(request):
    return HttpResponse("Book")

def reservation_details(request):
    return HttpResponse("Reservation details")