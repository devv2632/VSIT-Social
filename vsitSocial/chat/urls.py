from django.urls import path
from . import views
from chat import views as chat_views

urlpatterns = [
    path('home/' , views.index , name='home'),
    path('' , views.login_view , name='login'),
    path('signup/' ,views.signup_view ,name='signup'),
    path('signup/check_username/' ,views.check_username_view ,name='check_username'),
    path('home/create_confession/' ,views.create_confession ,name='create_confession'),
    path('home/account/' ,views.account_info ,name='account_info'),
    path('home/account/update/' ,views.update_account ,name='update_account'),
    path('logout/', views.logout_view, name='logout'),
    path('home/account/forgot_password/', views.forgot_password, name='forgot_password'),
    path('home/chat', views.chat, name='chat')
]