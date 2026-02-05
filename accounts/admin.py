from django.contrib import admin
from accounts.models import CustomUser

class AdminUser(admin.ModelAdmin):
    list_display=['email','phone','name','userprofile']

admin.site.register(CustomUser,AdminUser)