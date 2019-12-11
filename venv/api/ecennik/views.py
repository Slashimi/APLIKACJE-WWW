# from django.shortcuts import render

# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import viewsets
# from .models import Wyborcy, Kandydaci, Wojewodztwo, Partie
# from .selializers import WyborcySerializer, KandydaciSerializer, WojewodztwoSerializer, PartieSerializer


from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

from rest_framework import viewsets
from .models import Towary, Kupony
from .selializers import TowarySerializer, KuponySerializer

from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import F


class TowaryView(viewsets.ModelViewSet):
    #def get(self, request):
    queryset = Towary.objects.all()
    serializer_class = TowarySerializer


class KuponyView(viewsets.ModelViewSet):
    queryset = Kupony.objects.all()
    serializer_class = KuponySerializer

# Create your views here.
@api_view(["POST"])
def KuponyShow(data):
    print("1")
    lista_kuponow = Kupony.objects.all()
    print(lista_kuponow)
    stringus = ""
    for i in lista_kuponow:
        stringus += i.nazwa+" | "
        stringus += i.opis+" | "
        stringus += i.kod+" /// "
    
    return JsonResponse(stringus,safe=False)



@api_view(["POST"])
def Cennik(data):
    print("1")
    print(data)
    d = JSONParser().parse(data)

    lista = Towary.objects.all()
    print(lista)
    stringus = ""
    for i in lista:
        stringus += i.nazwa+" | "
        stringus += i.cena+" | "
        stringus += i.opis+" | "
        stringus += i.miasto+" | "
        stringus += i.marka+" | "
        stringus += i.kategoria+" /// "
    
    return JsonResponse(stringus,safe=False)


@api_view(["POST"])
def Marka(data):
    print("2")
    print(data)
    d = JSONParser().parse(data)
    marka = d['marka']
    print(marka)
    lista = Towary.objects.all().filter(marka=marka)
    print(lista)
    stringus = ""
    for i in lista:
        stringus += i.nazwa+" | "
        stringus += i.cena+" | "
        stringus += i.opis+" | "
        stringus += i.miasto+" | "
        stringus += i.marka+" | "
        stringus += i.kategoria+" /// "
    
    return JsonResponse(stringus,safe=False)
   

@api_view(["POST"])
def Kategoria(data):
    print("3")
    print(data)
    d = JSONParser().parse(data)
    kategoria = d['kategoria']
    print(kategoria)
    lista = Towary.objects.all().filter(kategoria=kategoria)
    print(lista)
    stringus = ""
    for i in lista:
        stringus += i.nazwa+" | "
        stringus += i.cena+" | "
        stringus += i.opis+" | "
        stringus += i.miasto+" | "
        stringus += i.marka+" | "
        stringus += i.kategoria+" /// "
    
    return JsonResponse(stringus,safe=False)
   

@api_view(["POST"])
def Miasto(data):
    print("3")
    print(data)
    d = JSONParser().parse(data)
    miasto = d['miasto']
    print(miasto)
    lista = Towary.objects.all().filter(miasto=miasto)
    print(lista)
    stringus = ""
    for i in lista:
        stringus += i.nazwa+" | "
        stringus += i.cena+" | "
        stringus += i.opis+" | "
        stringus += i.miasto+" | "
        stringus += i.marka+" | "
        stringus += i.kategoria+" /// "
    
    return JsonResponse(stringus,safe=False)
   
