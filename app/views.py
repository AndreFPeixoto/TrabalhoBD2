from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from app.models import User, Group
from .forms import CreateAccountForm, EnterForm, UpdateUserForm, GroupFrom

# Create your views here.
def welcome(request):
    return render(request, 'app/welcome.html')

def enter(request):
    if request.method == 'POST':
        form = EnterForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('url_home')
    else:
        form = EnterForm()
    return render(request, 'app/enter.html', {'form': form})

def create_account(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_enter')
    else:
        form = CreateAccountForm()
    return render(request, 'app/create_account.html', {'form': form})

def home(request):
    data = {}
    if request.user.is_authenticated:
        data['current_user'] = request.user
        return render(request, 'app/home.html', data)
    else:
        return redirect('url_welcome')

def exit(request):
    logout(request)
    return redirect('url_welcome')

def create_user(request):
    data = {}
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateAccountForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('url_home')
        else:
            form = CreateAccountForm()
        data['form'] = form
        data['btn_message'] = 'Criar'
        data['legend'] = 'Criar utilizador'
        return render(request, 'app/form_user.html', data)
    else:
        return redirect('url_welcome')
        
def read_user(request):
    data = {}
    if request.user.is_authenticated:
        data['current_user'] = request.user
        data['users'] = User.objects.all()
        return render(request, 'app/list_user.html', data)
    else:
        return redirect('url_welcome')
    
def update_user(request, pk):
    data = {}
    if request.user.is_authenticated:
        if request.user.is_admin:
            user = User.objects.get(pk=pk)
            user.set_unusable_password()
            form = UpdateUserForm(request.POST or None, instance=user)
            if form.is_valid():
                form.save()
                return redirect('url_read_user')
            data['form'] = form
            data['btn_message'] = 'Editar'
            data['legend'] = 'Editar utilizador'
            return render(request, 'app/form_user.html', data)
        else:
            return redirect('url_home')
    else:
        return redirect('url_welcome')

def delete_user(request, pk):
    if request.user.is_authenticated:
        if request.user.is_admin:
            user = User.objects.get(pk=pk)
            user.delete()
            return redirect('url_read_user')
        else:
            return redirect('url_home')
    else:
        return redirect('url_welcome')

def create_group(request):
    data = {}
    if request.user.is_authenticated:
        if request.user.is_admin:
            form = GroupFrom(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('url_home')
            data['form'] = form
            data['btn_message'] = 'Criar'
            data['legend'] = 'Criar grupo'
            return render(request, 'app/form_group.html', data)
        else:
            return redirect('url_home')
    else:
        return redirect('url_welcome')

def read_group(request):
    data = {}
    if request.user.is_authenticated:
        data['current_user'] = request.user
        data['groups'] = Group.objects.all()
        return render(request, 'app/list_group.html', data)
    else:
        return redirect('url_welcome')

def update_group(request, pk):
    data = {}
    if request.user.is_authenticated:
        if request.user.is_admin:
            group = Group.objects.get(pk=pk)
            form = GroupFrom(request.POST or None, instance=group)
            if form.is_valid():
                form.save()
                return redirect('url_read_group')
            data['form'] = form
            data['btn_message'] = 'Editar'
            data['legend'] = 'Editar grupo'
            return render(request, 'app/form_group.html', data)
        else:
            return redirect('url_home')
    else:
        return redirect('url_welcome')

def delete_group(request, pk):
    if request.user.is_authenticated:
        if request.user.is_admin:
            group = Group.objects.get(pk=pk)
            group.delete()
            return redirect('url_read_group')
        else:
            return redirect('url_home')
    else:
        return redirect('url_welcome')