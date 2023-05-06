"""mybits URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import *
from django.conf.urls.static import static
from django.conf import settings
from web.views import add_restaurant, restaurant_list
import web.views as wb

from django.contrib.auth import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('', wb.home, name='Home'),

    path('restaurant/', wb.restaurant_list, name='restaurant-list'),
    path('restaurant/<int:id_rest>/', wb.restaurant_detail, name='restaurant-detail'),

    path('localization/', wb.localization_list, name='localization-list'),
    path('localization/<int:id_loc>/', wb.localization_detail, name='localization-detail'),

    path('client/', wb.client_list, name='client-list'),
    path('client/<int:id_client>/', wb.client_detail, name='client-detail'),

    path('reservation/', wb.reservation_list, name='reservation-list'),
    path('reservation/<int:id_book>/', wb.reservation_detail, name='reservation-detail'),

    path('order/', wb.order_list, name='order-list'),
    path('order/<int:id_order>/', wb.order_detail, name='order-detail'),

    path('menu/', wb.menu_list, name='menu-list'),
    path('menu/<int:id_menu>/', wb.menu_detail, name='menu-detail'),

    path('login/', wb.login, name='login-menu'),
    path('login/register/', wb.register, name='register-menu'),

    path('admin/', admin.site.urls),

    path('about_us/', wb.about, name='about-us'),

    path('restaurant/create/', wb.add_restaurant, name='restaurant'),

    path('accounts/login', wb.LoginView.as_view(), name='login'),
    path('accounts/register', wb.register, name='register'),
    path('accounts/login', wb.LogoutView.as_view(), name='logout'),
    
]

# path('search/', search_bar, name='content_search'),
# Quan un usuari visiti la funcio de busqueda (lupa), llavors s'executara la funció search_bar, que estara dintre de views.py

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)