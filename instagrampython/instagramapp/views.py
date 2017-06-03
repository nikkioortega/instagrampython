from django.shortcuts import render, redirect
from instagramapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index ( request ):
    return render(request,'Rigistro.html')

def crear_usuario ( request ):
    _email = request.POST [ 'email' ]
    _username = request.POST [ 'username' ]
    _name = request.POST [ 'name' ]
    _password = request.POST [ 'password' ]
    print (_email)
    print (_name)
    print (_username)
    print (_password)
    user= User.objects.create_user ( username = _username, password = _password, email = _email, first_name = _name)
    myUser = MiUsuario ( usuario = user )
    myUser.save()
    print (user)
    print (user.password)
    return redirect ('login')

@login_required
def home (request):
    return render(request,'home.html')
