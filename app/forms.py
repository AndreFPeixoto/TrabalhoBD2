from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

class CreateAccountForm(UserCreationForm):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    password2 = forms.CharField(label='Confirmar Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['name', 'email']

class EnterForm(AuthenticationForm):
    class Meta:
        model = User

class UpdateUserForm(UserCreationForm):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    is_active = forms.BooleanField(label='Ativo')
    is_admin = forms.BooleanField(label='Administrador')
    password2 = forms.CharField(label='Confirmar Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['name', 'email', 'is_active', 'is_admin']