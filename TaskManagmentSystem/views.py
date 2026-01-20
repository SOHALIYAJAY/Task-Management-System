from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import ListView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# from Task.models import Tasklist
from django.views.generic import CreateView

class home(LoginRequiredMixin,TemplateView):
    template_name='home.html'
    login_url=reverse_lazy('login')

class task(LoginRequiredMixin,TemplateView):
    template_name='task.html'
    login_url=reverse_lazy('login')

# class taskcreate(LoginRequiredMixin, CreateView):
#     model = Tasklist
#     template_name = 'task.html'
#     success_url = reverse_lazy('home')
#     login_url = reverse_lazy('login')

#     fields = ['title', 'description', 'priority', 'status', 'due_date']

class dashboard(LoginRequiredMixin,TemplateView):
    template_name='dashboard.html'
    login_url=reverse_lazy('login')

class userlogout(TemplateView):
    template_name='logout.html'

class profile(TemplateView):
    template_name='profile.html'