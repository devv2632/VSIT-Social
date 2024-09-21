from django.shortcuts import render , redirect
from .models import Confessions
from django.contrib.auth import login , logout , authenticate 
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib import messages



def index(request):
    if not request.user.is_authenticated:
        raise Http404("User not logged in")
    else:
        ordered_confessions = Confessions.objects.all().order_by('-created_at')
        return render(request , 'index.html' ,{'confessions' : ordered_confessions})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        logout(request)
        return redirect('login')
    
def signup_view(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('Password')
       email = request.POST.get('email') 
       
       if User.objects.filter(username=username).exists():
           messages.error(request ,'Username exists')
       else:
           user = User.objects.create_user(username=username ,password=password ,email=email)
           user.save()
           return redirect('login')
    return render(request ,'signup.html')   

def check_username_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.error(request ,'Username exists') 
        else:
            messages.success(request ,'Username available')
    return render(request ,'checkUsername.html')

def create_confession(request):
    if request.method == 'POST':
        confess = request.POST.get('confess')
        username = request.user.username
        new_confession = Confessions(confess=confess ,username=username)
        new_confession.save()
        return redirect('home')

    return render(request ,'create_confession.html')
          

