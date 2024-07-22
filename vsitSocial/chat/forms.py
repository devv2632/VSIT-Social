from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class signup_form(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=50, required=True)
    roll_no = forms.CharField(max_length=11, required=True)
    DEPT = [
        ('BScIT', 'BScIT'),
        ('BScDS', 'BScDS'),
        ('BMS', 'BMS')
    ]
    dept = forms.ChoiceField(choices=DEPT, required=True, label='Select Department')
    YEAR = [
        ('FY', 'FY'),
        ('SY', 'SY'),
        ('TY', 'TY')
    ]
    year = forms.ChoiceField(choices=YEAR, required=True, label='Select Year')
    DIV = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    ]
    div = forms.ChoiceField(choices=DIV, required=True, label='Select Div')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
