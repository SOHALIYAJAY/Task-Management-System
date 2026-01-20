from django.contrib import admin
from accounts.models import CustomUser

class AdminUser(admin.ModelAdmin):
    list_display=['email','age','phone']

admin.site.register(CustomUser,AdminUser)