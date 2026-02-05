from django.contrib import admin
from Task.models import Tasklist

class TaskAdmin(admin.ModelAdmin):
    list_display=['user','title','description','priority','status','due_date']

admin.site.register(Tasklist,TaskAdmin)