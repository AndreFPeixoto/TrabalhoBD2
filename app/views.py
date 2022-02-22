from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from app.models import User, Group, Notice
from .forms import CreateAccountForm, CreateAccountAsAdminForm, EnterForm, UpdateUserForm, UpdateCurrentUserForm, GroupFrom, NoticeForm

# Create your views here.
def welcome(request):
    data = {}
    data['notices'] = Notice.objects.all().order_by('-last_modified')
    return render(request, 'app/welcome.html', data)

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

def create_notice(request):
    data = {}
    if request.user.is_authenticated:
        form = NoticeForm(request.POST or None)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.user = User.objects.get(pk=request.user.id)
            notice.save()
            return redirect('url_home')
        data['form'] = form
        data['btn_message'] = 'Criar'
        data['legend'] = 'Criar notícia'
        return render(request, 'app/form_notice.html', data)
    else:
        return redirect('url_welcome')

def read_notice(request):
    data = {}
    if request.user.is_authenticated:
        data['current_user'] = request.user
        data['notices'] = Notice.objects.all().order_by('-last_modified')[:10]
        return render(request, 'app/list_notice.html', data)
    else:
        return redirect('url_welcome')

def update_notice(request, pk):
    data = {}
    if request.user.is_authenticated:
        notice = Notice.objects.get(pk=pk)
        if request.user.is_admin or request.user.id == notice.user.id:
            form = NoticeForm(request.POST or None, instance=notice)
            if form.is_valid():
                form.save()
                return redirect('url_read_notice')
            data['form'] = form
            data['btn_message'] = 'Editar'
            data['legend'] = 'Editar notícia'
            return render(request, 'app/form_notice.html', data)
        else:
            return redirect('url_home')
    else:
        return redirect('url_welcome')

def delete_notice(request, pk):
    if request.user.is_authenticated:
        notice = Notice.objects.get(pk=pk)
        if request.user.is_admin or request.user.id == notice.user.id:
            notice.delete()
            return redirect('url_read_notice')
        else:
            return redirect('url_home')
    else:
        return redirect('url_welcome')

# Special views
def update_current_user(request, pk):
    data = {}
    if request.user.is_authenticated:
        user = User.objects.get(pk=pk)
        user.set_unusable_password()
        if request.user.is_admin:
            form = UpdateUserForm(request.POST or None, instance=user)
            if form.is_valid():
                current_user = form.save()
                login(request, current_user)
                return redirect('url_home')
        elif request.user.id == user.id:
            form = UpdateCurrentUserForm(request.POST or None, instance=user)
            if form.is_valid():
                current_user = form.save()
                login(request, current_user)
                return redirect('url_home')
        else:
            return redirect('url_home')
        data['form'] = form
        data['btn_message'] = 'Editar'
        data['legend'] = 'Editar utilizador'
        return render(request, 'app/form_user.html', data)
    else:
        return redirect('url_welcome')

def delete_current_user(request, pk):
    if request.user.is_authenticated:
        user = User.objects.get(pk=pk)
        if request.user.id == user.id:
            logout(request)
            user.delete()
            return redirect('url_welcome')
        else:
            return redirect('url_home')
    else:
        return redirect('url_welcome')

def read_notice_by_user(request, pk):
    data = {}
    if request.user.is_authenticated:
        user = User.objects.get(pk=pk)
        data['current_user'] = request.user
        data['notices'] = Notice.objects.filter(user=user).order_by('-last_modified')[:10]
        return render(request, 'app/list_notice.html', data)
    else:
        return redirect('url_welcome')

def read_notice_by_group(request, pk):
    data = {}
    if request.user.is_authenticated:
        group = Group.objects.get(pk=pk)
        data['current_user'] = request.user
        data['notices'] = Notice.objects.filter(group=group).order_by('-last_modified')[:10]
        return render(request, 'app/list_notice.html', data)
    else:
        return redirect('url_welcome')