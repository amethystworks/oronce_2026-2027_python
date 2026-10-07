from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser): 
    avatar = models.ImageField("", upload_to='user/avatar', null=True, blank=True)
    birth_dare = models.DateField(null=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.username