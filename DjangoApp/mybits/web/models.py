from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    id_restaurant = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    longitude = models.FloatField(max_length=50)  # Define tu valor predeterminado aquí
    latitude = models.FloatField(max_length=50)  # Define tu valor predeterminado aquí
    ranking = models.FloatField(max_length=50,null=True)  # Define tu valor predeterminado aquí

    
class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    DNI_NIE = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    card_number = models.CharField(max_length=50)

class Reservation(models.Model):
    id_reservation = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    people_num = models.IntegerField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
class Product(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    description=models.CharField(max_length=50)


class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    id_order = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)  # Hacer el campo nullable si es necesario
    quantity = models.IntegerField()
