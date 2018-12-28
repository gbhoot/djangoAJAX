from django.core.exceptions import ValidationError
from django.db import models

def validateNotEmpty(value):
    if not len(value):
        raise ValidationError(
            '{} must not be empty'.format(value)
        )

def validateLength(value):
    if len(value) < 5:
        raise ValidationError(
            '{} must be at least 5 characters long'.format(value)
        )

# Create your models here.
class Post(models.Model):
    note = models.TextField(blank=True, validators = [validateNotEmpty, validateLength])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)