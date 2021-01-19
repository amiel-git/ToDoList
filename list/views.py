from django.shortcuts import render
from list.models import Task

from django.urls import reverse
from django.http import HttpResponseRedirect

from core.models import UserProfileInfo
from django.contrib.auth.models import User
from list.models import Task
from django.contrib.auth.decorators import login_required


@login_required
def create_task_view(request):


    if request.method == "POST":

        title = request.POST.get('title')
        current_user = User.objects.get(id=request.user.id)
       
        task = Task(title=title,user=current_user)
        task.save()
        
        return HttpResponseRedirect(reverse('core:index'))

    
def delete_task_view(request,id):

    task = Task.objects.get(id=id)
    task.delete()
    
    return HttpResponseRedirect(reverse('core:index'))