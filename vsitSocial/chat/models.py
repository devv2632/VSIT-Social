from django.db import models
from django.contrib.auth.models import User

    
class Confessions(models.Model):
    confess = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f'confession by {self.username}'
        
