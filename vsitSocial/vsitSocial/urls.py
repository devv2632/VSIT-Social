from django.contrib import admin
from django.urls import path , include

admin.site.site_header = "Vsit Social Admin"
admin.site.site_title = "Vsit Social Admin Portal"
admin.site.index_title = "Welcome to Vsit Social"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('chat.urls'))
]
