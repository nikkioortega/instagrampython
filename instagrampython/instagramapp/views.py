from django.shortcuts import render

# Create your views here.
def index ( request ):
        return render(request,'Rigistro.html')

def login ( request ):
        return render(request,'Login.html')

def crear_usuario ( request ):
    print (request.POST)
