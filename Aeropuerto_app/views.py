from django.shortcuts import render
from Aeropuerto_app.models import *
from Aeropuerto_app.serializers import *
from rest_framework import viewsets, status

class Avion_view(viewsets.ModelViewSet):
    queryset = Avion.objects.all().order_by('codigo_avion')
    serializer_class = Avion_Serializer

class Piloto_view(viewsets.ModelViewSet):
    queryset = Piloto.objects.all().order_by('codigo_piloto')
    serializer_class = Piloto_Serializer