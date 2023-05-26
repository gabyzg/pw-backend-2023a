from django.shortcuts import render
# se importa http respone 
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hola desde mi primera vista 🎇")
def author(request):
    return HttpResponse("Autor: Gabriela Zavala Guerrero❤️")