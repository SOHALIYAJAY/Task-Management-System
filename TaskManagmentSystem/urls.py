"""
URL configuration for TaskManagmentSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TaskManagmentSystem import views
from django.contrib.auth.views import LoginView,LogoutView
from accounts.views import Usercreate
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home.as_view(),name='home'),
    path('login/', LoginView.as_view(template_name='userlogin.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/', Usercreate.as_view(),name='register'),
    path('taskcreate/',views.taskcreate,name='taskcreate'),
    path('mydashboard/',views.dashboard.as_view(),name='dashboard'),
    path('userlogout/',views.userlogout.as_view(),name='userlogout'),
    path('myprofile/',views.userprofile.as_view(),name='profile'),
    path('mytask/',views.taskconect.as_view(),name='mytask'),
    path('task/delete/<int:pk>/',views.deletetask.as_view(),name='taskdelete'),
    path('searchmytask/',views.searchtask.as_view(),name='searchmytask'),
    path('task/update/<int:pk>',views.updatetask.as_view(),name='updatetask'),
    path('mycompletetask/',views.completetask.as_view(),name='completetask'),
    path('completetask/',views.completetask.as_view(),name='completetask'),
    path('changetask/<int:pk>/',views.changetask.as_view(),name='changetask'),
    path('chageprofile/',views.chageprofile,name='chageprofile')

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)