from email.mime import image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to='avatares', null=False, blank=True)