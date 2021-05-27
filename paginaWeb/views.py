from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'paginaWeb/index.html')

def historia(request):
    return render(request,'paginaWeb/historia.html')

def galeria(request):
    return render(request,'paginaWeb/galeria.html')

def nosotros(request):
    return render(request,'paginaWeb/nosotros.html')

def contacto(request):
    return render(request,'paginaWeb/contacto.html')



