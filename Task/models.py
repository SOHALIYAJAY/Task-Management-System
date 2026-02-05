from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.contrib.auth import get_user_model

User=get_user_model()

class Tasklist(models.Model):
    PRIORITY_CHOICE=(
        ('High','High'),
        ('Medium','Medium'),
        ('Low','Low')
        )
    STATUS_CHOICE=(
        ('Pending','Pending'),
        ('Completed','Completed')
        )
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='tasks')
    title=models.CharField(max_length=40,null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    priority=models.CharField(default='Medium',choices=PRIORITY_CHOICE,max_length=10)
    status=models.CharField(default='Pending',choices=STATUS_CHOICE,max_length=10)
    due_date=models.DateField(name='due_date',null=True,blank=True)