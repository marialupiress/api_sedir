from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from todolist.models import todoitem
from todolist.serializes import todoitemserializer


class todoviewset(viewsets.ModelViewSet) :
#colocar ininciais maiusculas
    serializer_class = todoitemserializer
    queryset = todoitem.objects.all()
