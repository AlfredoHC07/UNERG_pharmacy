from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    rif = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    checked = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True)