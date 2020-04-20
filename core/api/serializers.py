from rest_framework.serializers import ModelSerializer
from core.models import Usuario,Preguntas

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model= Usuario
        fields=['nroencuesta','nombre','apellido','correo','empresa','telefono','fecha']

class PreguntasSerializer(ModelSerializer):
    class Meta:
        model= Preguntas
        fields=['nroencuesta','calidad','presentacion','sabor','temperatura','eficiencia',
        'agilidad','ambientacion','nroencuesta','expectativa','motivo','prox_visita','nroencuesta',
        'experiencia','funcionario','comentarios']


