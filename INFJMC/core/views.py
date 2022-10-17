from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # html = "<h1>Informática USM</h1> <a href='{% url 'carreras' %}'>Carreras</a>"
    # return HttpResponse(html)
    return render(request,'core/swag.html')

def carreras(request):
    html = "<h1>Carreras</h1>"
    return HttpResponse(html)

def docentes(request):
    html = "<h1>Docentes</h1>"
    return HttpResponse(html)