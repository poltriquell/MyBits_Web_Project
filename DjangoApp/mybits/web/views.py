from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.forms import UserCreationForm


def home(request):
    all_restaurants = Restaurant.objects.all()
    return render(request, 'html/home.html', {"restaurants" : all_restaurants})

#Restaurants
def restaurant_list(request):
    all_restaurants = Restaurant.objects.all()
    return render(request, 'html/restaurants.html', {"restaurants" : all_restaurants})

def restaurant_detail(request, id_rest):
    one_restaurant = Restaurant.objects.get(pk=id_rest)
    return render(request, 'html/restaurant.html', {"restaurant" : one_restaurant})

#Localizations
def localization_list(request):
    all_localizations = Localization.objects.all()
    return render(request, 'html/localizations.html', {"localizations" : all_localizations})

def localization_detail(request, id_loc):
    one_localization = Localization.objects.get(pk=id_loc)
    return render(request, 'html/localization.html', {"localization" : one_localization})

#Clients
def client_list(request):
    all_clients = Client.objects.all()
    return render(request, 'html/clients.html', {"clients" : all_clients})

def client_detail(request, id_client):
    one_client = Client.objects.get(pk=id_client)
    return render(request, 'html/client.html', {"client" : one_client})

#Reservations
def reservation_list(request):
    all_reservations = Reservation.objects.all()
    return render(request, 'html/reservations.html', {"reservations" : all_reservations})

def reservation_detail(request, id_book):
    one_reservation = Reservation.objects.get(pk=id_book)
    return render(request, 'html/reservation.html', {"reservation" : one_reservation})

#Orders
def order_list(request):
    all_orders = Order.objects.all()
    return render(request, 'html/orders.html', {"orders" : all_orders})

def order_detail(request, id_order):
    one_order = Order.objects.get(pk=id_order)
    return render(request, 'html/order.html', {"order" : one_order})

#Menus
def menu_list(request):
    all_menus = Menu.objects.all()
    return render(request, 'html/menus.html', {"menus" : all_menus})

def menu_detail(request, id_rest):
    one_menu = Menu.objects.get(pk=id_rest)
    return render(request, 'html/menu.html', {"menus" : one_menu})

#Login
def login(request):
    return render(request, 'html/login.html', None)

# def register(request):
#   return render(request, 'web/register.html', None)

#About Us
def about(request):
    return render(request, 'html/about.html', None)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'html/signup.html', {'form': form})

@login_required
def add_restaurant(request):
    form = RestaurantForm(request.POST or None)
    if form.is_valid():
        restaurant = form.save(commit=False)
        restaurant.user = request.user # set the user field to the current user
        restaurant.save()
        return redirect('restaurant_list', pk=restaurant.pk)
    return render(request, 'html/add_restaurant.html', {'form': form})

def restaurant_list(request):
    restaurants = Restaurant.objects.all() # obtiene todos los restaurantes de la base de datos
    context = {'restaurants': restaurants} # crea un diccionario de contexto que contiene la lista de restaurantes
    return render(request, 'html/restaurant_list.html', context) # renderiza la plantilla restaurant_list.html con el diccionario de contexto

from urllib.parse import urlparse, urlunparse

from django.conf import settings

# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import REDIRECT_FIELD_NAME, get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import url_has_allowed_host_and_scheme, urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

UserModel = get_user_model()


class RedirectURLMixin:
    next_page = None
    redirect_field_name = REDIRECT_FIELD_NAME
    success_url_allowed_hosts = set()

    def get_success_url(self):
        return self.get_redirect_url() or self.get_default_redirect_url()

    def get_redirect_url(self):
        """Return the user-originating redirect URL if it's safe."""
        redirect_to = self.request.POST.get(
            self.redirect_field_name, self.request.GET.get(self.redirect_field_name)
        )
        url_is_safe = url_has_allowed_host_and_scheme(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else ""

    def get_success_url_allowed_hosts(self):
        return {self.request.get_host(), *self.success_url_allowed_hosts}

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            return resolve_url(self.next_page)
        raise ImproperlyConfigured("No URL to redirect to. Provide a next_page.")

class LoginView(RedirectURLMixin, FormView):
    """
    Display the login form and handle the login action.
    """

    form_class = AuthenticationForm
    authentication_form = None
    template_name = "registration/login.html"
    redirect_authenticated_user = False
    extra_context = None

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            return resolve_url(self.next_page)
        else:
            return resolve_url(settings.LOGIN_REDIRECT_URL)

    def get_form_class(self):
        return self.authentication_form or self.form_class

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update(
            {
                self.redirect_field_name: self.get_redirect_url(),
                "site": current_site,
                "site_name": current_site.name,
                **(self.extra_context or {}),
            }
        )
        return context


class LogoutView(RedirectURLMixin, TemplateView):
    """
    Log out the user and display the 'You are logged out' message.
    """

    http_method_names = ["post", "options"]
    template_name = "registration/logged_out.html"
    extra_context = None

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        auth_logout(request)
        redirect_to = self.get_success_url()
        if redirect_to != request.get_full_path():
            # Redirect to target page once the session has been cleared.
            return HttpResponseRedirect(redirect_to)
        return super().get(request, *args, **kwargs)

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            return resolve_url(self.next_page)
        elif settings.LOGOUT_REDIRECT_URL:
            return resolve_url(settings.LOGOUT_REDIRECT_URL)
        else:
            return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update(
            {
                "site": current_site,
                "site_name": current_site.name,
                "title": _("Logged out"),
                "subtitle": None,
                **(self.extra_context or {}),
            }
        )
        return context


def logout_then_login(request, login_url=None):
    """
    Log out the user if they are logged in. Then redirect to the login page.
    """
    login_url = resolve_url(login_url or settings.LOGIN_URL)
    return LogoutView.as_view(next_page=login_url)(request)


def redirect_to_login(next, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Redirect the user to the login page, passing the given 'next' page.
    """
    resolved_url = resolve_url(login_url or settings.LOGIN_URL)

    login_url_parts = list(urlparse(resolved_url))
    if redirect_field_name:
        querystring = QueryDict(login_url_parts[4], mutable=True)
        querystring[redirect_field_name] = next
        login_url_parts[4] = querystring.urlencode(safe="/")

    return HttpResponseRedirect(urlunparse(login_url_parts))


# Class-based password reset views
# - PasswordResetView sends the mail
# - PasswordResetDoneView shows a success message for the above
# - PasswordResetConfirmView checks the link the user clicked and
#   prompts for a new password
# - PasswordResetCompleteView shows a success message for the above