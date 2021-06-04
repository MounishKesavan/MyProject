from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Resume(models.Model):
    name = models.CharField(max_length=235)
    email =  models.EmailField(max_length=70,blank=True)
    phone_number = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])

    def __str__(self):
        return self.name