from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from app_empresa.models import Patrimonio, Ambiente, Area, OrdemDeServico 

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 

    def create(self, validated_data):    
        validated_data['password'] = make_password(validated_data['password'])
        # Criar e retornar o usuário
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password'] 
        extra_kwargs = {'password': {'write_only': True}}

class PatrimonioSerializer(serializers.ModelSerializer):	
    class Meta:		
        model = Patrimonio		
        fields = '__all__' 
        
class AmbienteSerializer(serializers.ModelSerializer):	
    class Meta:		
        model = Ambiente		
        fields = '__all__' 

class AreaSerializer(serializers.ModelSerializer):	
    class Meta:		
        model = Area		
        fields = '__all__' 


class OrdemDeServicoSerializer(serializers.ModelSerializer):	
    class Meta:		
        model = OrdemDeServico		
        fields = '__all__' 

