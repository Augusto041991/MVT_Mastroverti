from django.shortcuts import render
from MVT_Mastroverti_Augusto.models import Familiar
from django.http import HttpResponse
from django.template import Template, loader

# Create your views here.

def familiar(request):

    familiar1=Familiar(nombre="Ramon", edad=24, profesion="zapatero")
    familiar1.save()
    texto1=f"Familiar 1 creado, nombre: {familiar1.nombre} ,edad: {familiar1.edad} ,profesion: {familiar1.profesion}.     "
    

    familiar2=Familiar(nombre="Manuela", edad=10, profesion="estudiante")
    familiar2.save()
    texto2=f"Familiar 2 creado, nombre: {familiar2.nombre} ,edad: {familiar2.edad} ,profesion: {familiar2.profesion}.      "
    
    familiar3=Familiar(nombre="Jazmin", edad=29, profesion="biologa")
    familiar3.save()
    texto3=f"Familiar 3 creado, nombre: {familiar3.nombre} ,edad: {familiar3.edad} ,profesion {familiar3.profesion}"

    return HttpResponse(texto1+texto2+texto3)






def html(self):

    familiar1=Familiar(nombre="Ramon", edad=24, profesion="zapatero")
    familiar1.save()
    
    familiar2=Familiar(nombre="Manuela", edad=10, profesion="estudiante")
    familiar2.save()
      
    familiar3=Familiar(nombre="Jazmin", edad=29, profesion="biologa")
    familiar3.save()

    diccionario={'nombre':[familiar1.nombre,familiar2.nombre,familiar3.nombre], 'edad':[familiar1.edad,familiar2.edad,familiar3.edad], 'profesion':[familiar1.profesion,familiar2.profesion,familiar3.profesion]}
        
    plantilla=loader.get_template('familiares.html')

    documento=plantilla.render(diccionario)

    return HttpResponse (documento)





