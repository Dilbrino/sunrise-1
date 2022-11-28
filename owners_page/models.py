from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here.
class CarOwner(models.Model):
    car_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(validators=[MinLengthValidator(8), MaxLengthValidator(12)], max_length=12)
    location = models.CharField(max_length=10)
    wallet = models.IntegerField(default=0)

    def __str__(self):
        return self.car_owner.first_name + ' ' + self.car_owner.last_name


gear_choice = (
    ('Manual', 'Manual'),
    ('Automatic', 'Automatic')
)


class Car(models.Model):
    car_name = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    owner = models.ForeignKey(CarOwner, on_delete=models.PROTECT)
    car_seats = models.IntegerField()
    gearbox = models.CharField(max_length=50, default='choose gearbox', choices=gear_choice)
    available_car = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    extra_info = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.car_name + ' ' + self.car_model