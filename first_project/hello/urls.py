#importar una biblioteca administradora de rutas 
from django.urls import path 

#importando vistas
from . import views

#declarando rutas validas 
#GEt hello /
urlpatterns = [
    path("", views.index, name="index"),
    #get /hello/author
    path("author/", views.author, name="author"),
    path("<str:name>", views.greet, name="greet")
]

