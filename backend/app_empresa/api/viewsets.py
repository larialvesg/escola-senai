from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from app_empresa.api import serializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from ..models import Patrimonio, Ambiente, Area, Gestor, Manutentor, OrdemDeServico 
from .serializers import PatrimonioSerializer, AmbienteSerializer, AreaSerializer, GestorSerializer, ManutentorSerializer, OrdemDeServicoSerializer, UserSerializer

class CreateUserAPIViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]


class PatrimonioViewSet(viewsets.ModelViewSet):     
    queryset = Patrimonio.objects.all()
    serializer_class = serializers.PatrimonioSerializer     
    # permission_classes = [IsAuthenticated]

class PatrimonioList(generics.ListAPIView):     
    queryset = Patrimonio.objects.all()
    serializer_class = serializers.PatrimonioSerializer     
    

class AmbienteViewSet(viewsets.ModelViewSet):     
    queryset = Ambiente.objects.all()
    serializer_class = serializers.AmbienteSerializer     
    # permission_classes = [IsAuthenticated]

class AmbienteList(viewsets.ListAPIView):     
    queryset = Ambiente.objects.all()
    serializer_class = serializers.AmbienteSerializer     
    

class GestorViewSet(viewsets.ModelViewSet):     
    queryset = Gestor.objects.all()
    serializer_class = serializers.GestorSerializer     
    # permission_classes = [IsAuthenticated]

class GestorList(viewsets.ListAPIView):     
    queryset = Gestor.objects.all()
    serializer_class = serializers.GestorSerializer     

class ManutentorViewSet(viewsets.ModelViewSet):     
    queryset = Manutentor.objects.all()
    serializer_class = serializers.ManutentorSerializer     
    # permission_classes = [IsAuthenticated]

class ManutentorList(viewsets.ListAPIView):     
    queryset = Manutentor.objects.all()
    serializer_class = serializers.ManutentorSerializer     
   

class OrdemDeServicoViewSet(viewsets.ModelViewSet):     
    queryset = OrdemDeServico.objects.all()
    serializer_class = serializers.OrdemDeServicoSerializer     
    # permission_classes = [IsAuthenticated]

class OrdemDeServicoList(generics.ListAPIView):     
    queryset = OrdemDeServico.objects.all()
    serializer_class = serializers.OrdemDeServicoSerializer 

class AreaViewSet(viewsets.ModelViewSet):     
    queryset = Area.objects.all()
    serializer_class = serializers.AreaSerializer     
    # permission_classes = [IsAuthenticated]

class AreaList(generics.ListAPIView):     
    queryset = Area.objects.all()
    serializer_class = serializers.AreaSerializer