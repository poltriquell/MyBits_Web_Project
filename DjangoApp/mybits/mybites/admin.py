from django.contrib import admin
from mybites.models import MyBite

# Register your models here.

admin.site.site_header = 'MyBites Administration'
admin.site.register(Restaurant)
admin.site.register(Localization)
admin.site.register(Meal)
admin.site.register(Client)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(Menu)




