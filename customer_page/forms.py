from django import forms
from owners_page.models import gear_choice

class SetPasswordForm(forms.Form):
    password = forms.CharField(max_length=40)

class customerForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=40)
    mobile = forms.CharField(max_length = 12)
    location = forms.CharField(max_length=10)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()

class filter(forms.Form):
    name = forms.CharField(required=False)
    model = forms.CharField(required=False)
    seats = forms.IntegerField(required=False)
    gearBox = forms.ChoiceField(choices=gear_choice, required=False)
    location = forms.CharField(required=False)

