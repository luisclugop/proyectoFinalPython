from django.http import HttpResponse
from django.shortcuts import render
import datetime
from AppCoder.models import Pokemon

def saludo(request): 
    return HttpResponse("Hola Coder")

def diaDeHoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es de dia: <br> {dia}"

    return HttpResponse(documentoDeTexto)

# def index(request):
#     nombre = "Luis"
#     apellido = "Lugo"
#     listas = [1,2,3,4,5,6]

#     contexto = {
#         "nombre": nombre, 
#         "apellido": apellido,
#         "listas": listas
#     }
#     return render(request, 'index.html', contexto)

def pokemon(request):
    pokemons = Pokemon(nombre="Caterpie", tipo="Bicho", numero="010")
    pokemons.save()

    contexto = {
        'pokemon1': pokemons
    }
    return render(request, 'index.html', contexto)
