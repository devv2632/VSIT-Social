from django.urls import path
from . import views
from chat import views as chat_views

urlpatterns = [
    path('home/' , views.index , name='home'),
    path('' , views.login_view , name='login'),
    path('signup/' ,views.signup_view ,name='signup'),
    path('signup/check_username/' ,views.check_username_view ,name='check_username'),
    path('home/create_confession' ,views.create_confession ,name='create_confession')
    
]