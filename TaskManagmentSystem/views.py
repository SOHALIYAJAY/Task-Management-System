from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import ListView,TemplateView,CreateView,DeleteView,View,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.admin import CustomUser
from Task.models import Tasklist

class home(LoginRequiredMixin,TemplateView):
    template_name='home.html'
    login_url=reverse_lazy('login')

# class task(LoginRequiredMixin,TemplateView):
#     template_name='task.html'
#     login_url=reverse_lazy('login')

# # class taskcreate(LoginRequiredMixin, CreateView):
# #     model = Tasklist
#     template_name = 'task.html'
#     success_url = reverse_lazy('home')
#     login_url = reverse_lazy('login')

#     fields = ['title', 'description', 'priority', 'status', 'due_date']

class dashboard(LoginRequiredMixin,TemplateView):
    template_name='dashboard.html'
    login_url=reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['task']=Tasklist.objects.all()
        context['totaltask']=Tasklist.objects.all().count()
        context['pendingtask']=Tasklist.objects.filter(status='Pending').count()
        context['completetask']=context['totaltask']-context['pendingtask']

        return context

class userlogout(TemplateView):
    template_name='logout.html'

class userprofile(TemplateView):
    template_name='profile.html'


def taskcreate(request):
    n={}
    if request.method == "POST":
        print("POST REQUEST RECEIVED") 
        title=request.POST.get('title')
        description=request.POST.get('description')
        priority=request.POST.get('priority')
        status=request.POST.get('status')
        due_date=request.POST.get('due_date')

        Tasklist.objects.create(title=title,description=description,priority=priority,status=status,due_date=due_date)
        print("TASK SAVED")   
        return render(request,'home.html')
    else:
        return render(request,'task.html')

class mytask(TemplateView):
    template_name='mytask.html'

        
class taskconect(ListView):
    model=Tasklist
    template_name='mytask.html'
    context_object_name='tasklist'
    def get_queryset(self):
        return Tasklist.objects.all()
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['totaltask']=Tasklist.objects.all().count()
        context['pendingtask']=Tasklist.objects.filter(status='Pending').count()
        context['completetask']=Tasklist.objects.all().count()-Tasklist.objects.filter(status='Pending').count()

        return context

class deletetask(DeleteView):
    model=Tasklist 
    success_url=reverse_lazy('mytask')

# def searchmytask(request):
#     TASK={}
#     if request.method=='POST':
#         taskname=request.POST.get('searchmytask')
#         newtask=Tasklist.objects.filter(title__icontains=taskname)
#         TASK={
#             "newtask":newtask
#         }
#         return render(request,"mytask.html",TASK)
#     newtask=Tasklist.objects.all
#     return render(request,"mytask.html",TASK)

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
    fields='__all__'
    template_name='updatetask.html'
    success_url=reverse_lazy('mytask')

class completetask(ListView):
    model=Tasklist
    template_name='completetask.html'
    context_object_name='task'

    def get_queryset(self):
        return Tasklist.objects.filter(status='Pending')