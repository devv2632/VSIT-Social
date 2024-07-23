from django.shortcuts import render , redirect
from .forms import signup_form
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
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                full_name=form.cleaned_data.get('full_name'),
                roll_no=form.cleaned_data.get('roll_no'),
                dept=form.cleaned_data.get('dept'),
                year=form.cleaned_data.get('year'),
                div=form.cleaned_data.get('div')
            )
            login(request, user)
            return redirect('')
    else:
        form = signup_form()
    return render(request, 'signup.html', {'form': form})
