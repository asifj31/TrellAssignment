from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import addmovieform
from .models import movies


def home(request):
    return render(request,'index.html')

def signupuser(request):
    if request.method =='GET':
        return render(request,'signupuser.html', { 'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('loginuser')
            except IntegrityError:
                return render(request,'signupuser.html', { 'form':UserCreationForm(), 'error':'USERNAME ALREADY TAKEN'})    
        else:
            return render(request,'signupuser.html', { 'form':UserCreationForm(), 'error':'PASSWORDS DO NOT MATCH'})

def loginuser(request):
    if request.method =='GET':
        return render(request,'loginuser.html', { 'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'loginuser.html', { 'form':AuthenticationForm(),'error':'Username and password did not match OR the user does not exists. Please recheck, else sign up!'})
        else:
            login(request,user)
            return redirect('mainpage')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')


def mainpage(request):
    movie= movies.objects.all()
    return render(request,'main.html', {'movie':movie})

def addmovies(request):
    if request.method == 'GET':
        return render(request,'addmovies.html', { 'form':addmovieform()})
    else:
        form = addmovieform(request.POST)
        form.save()
        return redirect('mainpage')