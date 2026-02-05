from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
from accounts.manager import CustomUserManager

class CustomUser(AbstractUser):
    username=None
    name=models.CharField(null=True,blank=True,max_length=15)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10,null=True,blank=True)
    userprofile=models.ImageField(upload_to='profile/',blank=True, null=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()
    
    def __str__(self):
        return self.email
    