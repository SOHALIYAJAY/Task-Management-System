# from django.db import models
# from accounts.views import User


# class Tasklist(models.Model):
#     PRIORITY_CHOICE=(
#         ('high','High'),
#         ('medium','Medium'),
#         ('low','Low')
#         )
#     STATUS_CHOICE=(
#         ('pending','Pending'),
#         ('in-progress','In Progress'),
#         ('completed','Completed')
#         )
#     # user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
#     title=models.CharField(max_length=40,null=True,blank=True)
#     description=models.CharField(max_length=200,null=True,blank=True)
#     priority=models.CharField(default='Medium',choices=PRIORITY_CHOICE)
#     status=models.CharField(default='Pending',choices=STATUS_CHOICE)
#     due_date=models.DateField(name='due_date',null=True,blank=True)