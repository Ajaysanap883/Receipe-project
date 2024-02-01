from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login_page/')
def receipe(request):
  #reading data
  if request.method=='POST':
    data=request.POST
    name=data.get('name')
    description=data.get('description')
    image=request.FILES.get('image')
  #creating object
    Receipe.objects.create(
      name=name,
      description=description,
      image=image,
      )
    
    return redirect('/receipe/')
  
  queryset=Receipe.objects.all()
  
 
 #search function
  if request.GET.get('search'):
    queryset=queryset.filter(name__icontains =request.GET.get('search'))

  context={'receipe':queryset}
  return render(request,'receipes/receipe.html',context)


def delete(request,id):
  queryset=Receipe.objects.get(id=id)
  queryset.delete()
  return redirect('/receipe/')


@login_required(login_url='/login_page/')  
def update(request,id):
# to get the clicked object
  queryset=Receipe.objects.get(id=id)

#get updated values
  if request.method=='POST':
      data=request.POST
      name=data.get('name')
      description=data.get('description')
      image=request.FILES.get('image')   

      queryset.name=name
      queryset.description=description
      
      if image:
        queryset.image=image
      
      queryset.save()
      return redirect('/receipe/') 


#queryset set me jo object liya usse render kara raha h page pe
  context={'receipe':queryset}

  return render(request,'receipes/update_receipe.html',context)

def register(request):
  if request.method=='POST':
    data=request.POST
    first_name=data.get('first_name')
    last_name=data.get('last_name')
    username=data.get('username')
    password=data.get('password')

    user=User.objects.filter(username=username)

    if user.exists():
      messages.info(request, "username already exist.")
      return redirect('/register/')

    else:
      user=User.objects.create(
      first_name=first_name,
      last_name=last_name,
      username=username,
      )
      user.set_password(password)
      user.save()

      messages.info(request, "account created successfully.")

      return redirect('/register/')

  return render(request,'register.html')


def login_page(request):
  if request.method=="POST":
    data=request.POST

    username=data.get('username')
    password=data.get('password')

    if not User.objects.filter(username=username).exists():
      messages.info(request, "invalid username")
      return redirect ('/login_page/')
    
    user=authenticate(username=username,password=password)

    if user is None:
      messages.error(request,"invalid password")
      return redirect ('/login_page/')
    else:
      login(request,user)
      return redirect('/receipe/')
  return render(request,'login.html')


def logout_page(request):
  logout(request)
  return redirect('/login_page/')





