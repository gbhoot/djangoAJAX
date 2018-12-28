from django.db import models
from django.core.exceptions import ValidationError




# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45, validators = [validateNotEmpty, validateLength, validateAlpha])
    last_name = models.CharField(max_length=45, validators = [validateNotEmpty, validateLength, validateAlpha])
    email = models.EmailField(max_length=45, validators = [validateNotEmpty, validateEmail])
    password = models.CharField(max_length=255, validators = [validateNotEmpty, validatePassLength])
    