from django.shortcuts import redirect, render
from django.contrib.auth import login
from .forms import CreateAccountForm, EnterForm

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
