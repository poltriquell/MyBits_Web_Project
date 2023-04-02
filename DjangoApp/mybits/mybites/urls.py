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
from mybites.views import * 


urlpatterns = [
    path("admin/", admin.site.urls),
    path("search/", views.activate_search_bar, name='search_content')
]

app_name = 'content'

urlpatterns = [
    path('search/go/', search_bar_redirect, name='content_search_go'),
    path('rating/create/', rating, name='rating'),
    path('rating/delete/<int:pk>/', AssesmentDeleteView.as_view(), name='delete-rating'),
    path('info/<int:pk>/', ContentDetailView.as_view(), name='info'),
    path('status/update/<int:content_id>/', update_status, name='update-status'),
    path('status/delete/<int:pk>/', StatusDeleteView.as_view(), name='delete-status'),
    path('platform/add/<int:id>/', PlatformContentCreateView.as_view(), name='add_in_platform'),
    path('platform/edit/<int:pk>/', PlatformContentUpdateView.as_view(), name='edit_in_platform'),
    path('platform/delete/<int:pk>/', PlatformContentDeleteView.as_view(), name='delete_in_platform'),
]

# path('search/', search_bar, name='content_search'),
# Quan un usuari visiti la funcio de busqueda (lupa), llavors s'executara la funció search_bar, que estara dintre de views.py