from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
from accounts.manager import CustomUserManager

class CustomUser(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    age=models.IntegerField(default=0)
    phone=models.CharField(max_length=10,null=True,blank=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()
    
    def __str__(self):
        return self.email
    