from dataclasses import fields
from django import forms
from .models import User, Group, Notice
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

class UpdateCurrentUserForm(UserCreationForm):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    password2 = forms.CharField(label='Confirmar Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['name', 'email']

class GroupFrom(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']
        labels = {
            'name': 'Nome',
            'description': 'Descrição'
        }

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'description', 'image_url', 'content', 'is_public', 'group']
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'image_url': 'URL Imagem',
            'content': 'Conteúdo',
            'is_public': 'Pública',
            'group': 'Grupo'
        }