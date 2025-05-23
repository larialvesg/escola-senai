from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from ..models import Patrimonio, Ambiente, Area, OrdemDeServico 
from .serializers import (
    PatrimonioSerializer, AmbienteSerializer, AreaSerializer, OrdemDeServicoSerializer,
    UserSerializer
)

class CreateUserAPIViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class PatrimonioViewSet(viewsets.ModelViewSet):     
    queryset = Patrimonio.objects.all()
    serializer_class = PatrimonioSerializer

class PatrimonioList(generics.ListAPIView):     
    queryset = Patrimonio.objects.all()
    serializer_class = PatrimonioSerializer

class AmbienteViewSet(viewsets.ModelViewSet):     
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer

class AmbienteList(generics.ListAPIView):     
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer


class OrdemDeServicoViewSet(viewsets.ModelViewSet):     
    queryset = OrdemDeServico.objects.all()
    serializer_class = OrdemDeServicoSerializer

class OrdemDeServicoList(generics.ListAPIView):     
    queryset = OrdemDeServico.objects.all()
    serializer_class = OrdemDeServicoSerializer

class AreaViewSet(viewsets.ModelViewSet):     
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class AreaList(generics.ListAPIView):     
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


