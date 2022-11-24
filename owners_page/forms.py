from django import forms
from .models import gear_choice, Car

class CarForm(forms.Form):
    car_name = forms.CharField(max_length=20)
    car_model = forms.CharField(max_length=20)
    car_seats = forms.IntegerField()
    gearbox = forms.ChoiceField(choices=gear_choice)
    price = forms.IntegerField()
    extra_info = forms.CharField(max_length=100)

class CarEditForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner','available_car','date_added' ]



class ownerForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=40)
    mobile = forms.CharField(max_length = 12)
    location = forms.CharField(max_length=10)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()

