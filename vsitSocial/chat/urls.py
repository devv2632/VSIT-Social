from django.urls import path
from . import views
from chat import views as chat_views

urlpatterns = [
    path('home' , views.index , name='home'),
    path('login' , views.login_view , name='login'),
    path('signup' , views.signup_view , name='signup'),
    path('', chat_views.chatPage, name='chat-page')
    
]