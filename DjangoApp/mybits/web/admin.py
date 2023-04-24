from django.contrib import admin
from .models import *

admin.site.register(Restaurant)
admin.site.register(Localization)
admin.site.register(Client)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(Menu)


class Restaurant_Manager(admin.StackedInline):
    model = Restaurant_Manager
    can_delete = True
    verbose_name_plural = "Restaurant_Manager"


admin.site.unregister(User)
admin.site.register(User, Restaurant_Manager)
