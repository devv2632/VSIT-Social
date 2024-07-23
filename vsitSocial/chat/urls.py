from django.urls import path
from . import views


urlpatterns = [
    path('home' , views.index , name='home'),
    path('' , views.login_view , name='login'),
    path('signup' , views.signup_view , name='signup')
]