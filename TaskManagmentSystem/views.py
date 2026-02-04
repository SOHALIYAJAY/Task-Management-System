from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import ListView,TemplateView,CreateView,DeleteView,View,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.admin import CustomUser
from Task.models import Tasklist
from django.contrib import messages

class home(LoginRequiredMixin,TemplateView):
    template_name='home.html'
    login_url=reverse_lazy('login')

class dashboard(TemplateView):
    template_name='dashboard.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        progress = 0
        user=self.request.user
        context['task']=Tasklist.objects.filter(user=self.request.user)
        context['totaltask']=Tasklist.objects.filter(user=self.request.user).count()
        context['pendingtask']=Tasklist.objects.filter(status='Pending',user=self.request.user).count()
        context['completetask']=context['totaltask']-context['pendingtask']
        # context['user']=CustomUser.objects.get(user=self.request.user)
        if context['totaltask'] > 0:
             progress = (context['completetask'] / context['totaltask']) * 100
        context['progress']=progress
        return context

class userlogout(TemplateView):
    template_name='logout.html'

class userprofile(TemplateView):
    template_name='profile.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['totaltask']=Tasklist.objects.filter(user=self.request.user).count()
        context['completetask']=Tasklist.objects.filter(status='Completed',user=self.request.user).count()
        context['pendingtask']=context['totaltask']-context['completetask']

        return context

def taskcreate(request):
    n={}
    if request.method == "POST":
        print("POST REQUEST RECEIVED") 
        user=request.POST.get('user')
        title=request.POST.get('title')
        description=request.POST.get('description')
        priority=request.POST.get('priority')
        status=request.POST.get('status')
        due_date=request.POST.get('due_date')

        Tasklist.objects.create(user=request.user,title=title,description=description,priority=priority,status=status,due_date=due_date)
        print("TASK SAVED")   
        messages.success(request,'Task Created Successfully')
        return render(request,'task.html')
    else:
        return render(request,'task.html')

class mytask(TemplateView):
    template_name='mytask.html'

        
class taskconect(ListView):
    model=Tasklist
    template_name='mytask.html'
    context_object_name='tasklist'
    def get_queryset(self):
        return Tasklist.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['totaltask']=Tasklist.objects.filter(user=self.request.user).count()
        context['pendingtask']=Tasklist.objects.filter(status='Pending',user=self.request.user ).count()
        context['completetask']=Tasklist.objects.filter(user=self.request.user).count()-Tasklist.objects.filter(status='Pending',user=self.request.user).count()

        return context

class deletetask(DeleteView):
    model=Tasklist 
    success_url=reverse_lazy('mytask')

class searchtask(ListView):
    model=Tasklist
    template_name='mytask.html'
    context_object_name='tasklist'
    def get_queryset(self):
        return Tasklist.objects.filter(title__icontains=self.request.GET.get('searchtask'))
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['totaltask']=Tasklist.objects.filter(title__icontains=self.request.GET.get('searchtask')).count()
        context['pendingtask']=Tasklist.objects.filter( title__icontains=self.request.GET.get('searchtask'),status='Pending' ).count()
        context['completetask']=context['totaltask']-context['pendingtask']

        return context
    
class updatetask(UpdateView,TemplateView):
    model=Tasklist
    fields=['title','description','priority','due_date']
    template_name='updatetask.html'
    success_url=reverse_lazy('mytask')

class completetask(ListView):
    model=Tasklist
    template_name='completetask.html'
    context_object_name='task'

    def get_queryset(self):
        return Tasklist.objects.filter(status='Pending',user=self.request.user) 
    
class changetask(View):
    def get(self,request,pk):
        tc=Tasklist.objects.get(pk=pk)
        tc.status='Completed'
        tc.save()
        return redirect('mytask')

def chageprofile(request):
    if request.method == 'POST':
        user=request.user
        user.name=request.POST.get('name')
        user.email=request.POST.get('email')
        user.phone=request.POST.get('phone')

        user.save()
        # user.refresh_from_db()
        return render(request,'profile.html')
    return HttpResponse('dgewg')