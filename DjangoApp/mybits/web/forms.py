from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    DNI_NIE = forms.CharField(max_length=50)
    address = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    card_number = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "name", "DNI_NIE", "address", "phone", "email", "card_number"]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            client = Client.objects.create(
                name=self.cleaned_data['name'],
                DNI_NIE=self.cleaned_data['DNI_NIE'],
                address=self.cleaned_data['address'],
                phone=self.cleaned_data['phone'],
                email=self.cleaned_data['email'],
                card_number=self.cleaned_data['card_number']
            )
            client.save()
        return user