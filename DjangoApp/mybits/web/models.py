from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    id_restaurant = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    id_localization = models.ForeignKey('Localization', on_delete=models.CASCADE)

class Localization(models.Model):
    id_localization = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)

class Meal(models.Model):
    id_dish_product = models.AutoField(primary_key=True)
    id_restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    DNI_NIE = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    card_number = models.CharField(max_length=50)
    num_reservation = models.IntegerField()

class Reservation(models.Model):
    id_reservation = models.AutoField(primary_key=True)
    date = models.DateField()
    people_num = models.IntegerField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    data= models.DateField()
    total_price = models.FloatField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)


class Menu(models.Model):
    id_dish_product = models.ForeignKey(Meal, on_delete=models.CASCADE)
    id_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    type = models.CharField(max_length=50)