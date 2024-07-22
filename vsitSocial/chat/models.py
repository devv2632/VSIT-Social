from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=11)
    DEPT_CHOICES = [
        ('BScIT', 'BScIT'),
        ('BScDS', 'BScDS'),
        ('BMS', 'BMS')
    ]
    dept = models.CharField(max_length=10, choices=DEPT_CHOICES)
    YEAR_CHOICES = [
        ('FY', 'FY'),
        ('SY', 'SY'),
        ('TY', 'TY')
    ]
    year = models.CharField(max_length=2, choices=YEAR_CHOICES)
    DIV_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    ]
    div = models.CharField(max_length=1, choices=DIV_CHOICES)
    

    def __str__(self):
        return self.user.username
