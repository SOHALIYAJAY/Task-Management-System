from django.shortcuts import render
from accounts.forms import UserRegistrationForm
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from accounts.models import CustomUser
from django.contrib import messages
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail
from accounts.models import CustomUser

User=get_user_model()

class Usercreate(CreateView):
    model=CustomUser
    template_name='registration.html'
    success_url=reverse_lazy('home')
    form_class=UserRegistrationForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        # send_mail(
        #     'Task Manager System',
        #     'Your Registration SuccesFully',
        #     'monata123123@gmail.com',
        #     ['jaysohaliya5726@gmail.com'],
        #     fail_silently=False,

        # )
        messages.success(self.request,"Your Registration SuccessFully ")
        return super().form_valid(form)
    