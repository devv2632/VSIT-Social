from django.shortcuts import render , redirect
from django.contrib import messages
from .models import Profile
from django.contrib.auth import login , logout , authenticate
from django.http import Http404


def index(request):
    if not request.user.is_authenticated:
        raise Http404("User not logged in")
    return render(request , 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful!')
            return redirect('')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        logout(request)
        return redirect('login')
    
def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}
    return render(request, "chat/chatPage.html", context)
