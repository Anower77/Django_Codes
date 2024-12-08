from django import forms
from django.forms.widgets import NumberInput
import datetime


FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class Form(forms.Form):
    title = forms.CharField()
    description = forms.CharField() 

    
    
    
    
    
    # favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    # favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    # value = forms.DecimalField()    
  	# day = forms.DateField(initial=datetime.date.today)
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    # birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    # date = forms.DateField()
    # agree = forms.BooleanField()
    # email: forms.EmailField()
    # comment = forms.CharField(widget=forms.Textarea(attrs={'row':3}))
    # comment = forms.CharField(widget=forms.Textarea)
    # name = forms.CharField()
# BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']


    
