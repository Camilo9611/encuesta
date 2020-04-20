from core.models import Usuario, Preguntas
from .serializers import UsuarioSerializer,PreguntasSerializer
from rest_framework import viewsets
from django.shortcuts import render, redirect
from rest_framework.response import Response

from django.contrib.auth.forms import AuthenticationForm as au
from django.contrib.auth import login
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.contrib.auth.decorators import login_required
from rest_framework import filters


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset= Usuario.objects.all()
    serializer_class= UsuarioSerializer
    authentication_classes= [SessionAuthentication, BasicAuthentication]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['nombre', 'apellido','correo','empresa']
    ordering_fields = ['nroencuesta', 'fecha']

class PreguntasViewSet(viewsets.ModelViewSet):
    queryset= Preguntas.objects.all()
    serializer_class= PreguntasSerializer
    authentication_classes= [SessionAuthentication, BasicAuthentication]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['nroencuesta__nroencuesta','nroencuesta__nombre','nroencuesta__apellido']
    ordering_fields = ['nroencuesta']

def login_api(request):
    if request.method =='POST':
        form =au(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('api/')
    else:
        form= au()
    return render(request,'registration/login.html',{'form':form})