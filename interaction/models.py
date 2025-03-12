from django.db import models
from django.core.validators import RegexValidator

iranian_phone_validator = RegexValidator(
    regex=r'^09\d{9}$',
    message="Phone number must be a valid Iranian number starting with 09 and containing 11 digits."
)

class User(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(
        max_length=11,
        validators=[iranian_phone_validator],
        unique=True 
    )

class Product(models.Model):
    name = models.CharField(max_length=20)
    seller = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    price = models.PositiveBigIntegerField()