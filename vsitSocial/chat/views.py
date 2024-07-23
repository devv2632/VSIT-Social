from django.shortcuts import render , redirect
from .forms import signup_form
from django.contrib import messages
from .models import Profile
from django.contrib.auth import login , logout

def index(request):
    return render(request , 'index.html')

def login_view(request):
    return render(request , 'login.html')

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
