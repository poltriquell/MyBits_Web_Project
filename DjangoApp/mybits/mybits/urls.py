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
from django.urls import path
import web.views as wb

urlpatterns = [
    path('',wb.home, name='Home'),
    path('admin/', admin.site.urls),
]
# path('search/', search_bar, name='content_search'),
# Quan un usuari visiti la funcio de busqueda (lupa), llavors s'executara la funció search_bar, que estara dintre de views.py

urlpatterns = [
    path('', home, name='home'),
    path('Teatre/', include('Teatre.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # User authentication
    path('SignIn/', SignIn, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),

    path('accounts/delete/', delete_user, name='delete_user'),
    path('usermanage/', user_management, name='user_management'),
]
from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)