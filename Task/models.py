from django.db import models
# from accounts.views import User


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

    title=models.CharField(max_length=40,null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    priority=models.CharField(default='Medium',choices=PRIORITY_CHOICE,max_length=10)
    status=models.CharField(default='Pending',choices=STATUS_CHOICE,max_length=10)
    due_date=models.DateField(name='due_date',null=True,blank=True)