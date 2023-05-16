from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    id_restaurant = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    longitude = models.FloatField(default=41.6)  # Define tu valor predeterminado aquí
    latitude = models.FloatField(default=0.6226)  # Define tu valor predeterminado aquí
    
class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True, default=1)
    description = models.CharField(max_length=50)
    id_restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    
class Localization(models.Model):
    id_localization = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, default="prova")
    name = models.CharField(max_length=50)
    DNI_NIE = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    card_number = models.CharField(max_length=50)

class Reservation(models.Model):
    id_reservation = models.AutoField(primary_key=True)
    date = models.DateField()
    people_num = models.IntegerField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    


class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

