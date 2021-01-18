from django.shortcuts import render

from core import forms
from list.models import Task

from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

@login_required()
def index(request):

    tasks = Task.objects.filter(user=request.user)
    current_user = request.user.username
    context = {"tasks":tasks,"user":current_user,"is_in":True}
    
    return render(request,'core/index.html',context)
        


def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)

            return HttpResponseRedirect(reverse('core:index'))


    return render(request,'core/login.html')


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('core:login'))


def register(request):
    user_form = forms.UserForm()
    user_profile_info_form = forms.UserProfileInfoForm()
    context = {
        "user_form":user_form,
        "user_profile_info_form":user_profile_info_form
        }


    if request.method == "POST":
        user_form = forms.UserForm(request.POST)
        user_profile_info_form = forms.UserProfileInfoForm(request.POST) 

        if user_form.is_valid() and user_profile_info_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_profile = user_profile_info_form.save(commit=False)
            user_profile.user = user

            if 'profile_pic' in request.FILES:
                user_profile.profile_pic = request.FILES['profile_pic']

            user_profile.save()

            return HttpResponseRedirect(reverse('core:login'))

    return render(request,'core/register.html',context)