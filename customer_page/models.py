from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

# Create your models here.
from owners_page.models import Car, CarOwner


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(validators = [MinLengthValidator(8), MaxLengthValidator(12)], max_length = 12)
    location = models.CharField(max_length=10)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    car_owner = models.ForeignKey(CarOwner, on_delete=models.PROTECT)
    rent = models.CharField(max_length=8)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    days = models.CharField(max_length=3)
    is_complete = models.BooleanField(default=False)

