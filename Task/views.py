from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from forms import taskform
from django.contrib.auth.mixins import LoginRequiredMixin

# class createtask(LoginRequiredMixin,CreateView):
#     form_class=taskform
#     template_name='task.html'
#     success_url=reverse_lazy('task')
#     login_url=reverse_lazy('login')