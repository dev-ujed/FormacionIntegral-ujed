from rest_framework import serializers 
from .models import FormacionIntegral
from Alumnos.models import Oalumno
 
 
class FormacionInSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormacionIntegral
        fields = ('id',  
                  'matricula',
                  'nombre', 
                  'asistencia',
                  'evento',
                  'alumno',
                  'created',
                  'modified',
                  
                  )

        #fields = '__all__'



class FormacionInEventoSerializer(serializers.ModelSerializer):
    unidadResponsable = serializers.CharField(source = 'evento.unidadResponsable')
    tituloEvento = serializers.CharField(source = 'evento.tituloEvento')
    descripcionEvento = serializers.CharField(source = 'evento.descripcionEvento')
    eventoDedicadoA = serializers.CharField(source = 'evento.eventoDedicadoA')
    #imagen = serializers.ImageField(upload_to='Eventos/images')
    #Calendario
    fechaEvento = serializers.DateField(source = 'evento.fechaEvento')
    inicioEvento = serializers.TimeField(source = 'evento.inicioEvento')
    finEvento = serializers.TimeField(source = 'evento.finEvento')
    sede = serializers.CharField(source = 'evento.sede')
    cupo = serializers.IntegerField(source = 'evento.cupo')
    descripcion = serializers.CharField(source = 'evento.descripcion')
    #Creditos
    creditos = serializers.DecimalField(source = 'evento.creditos', max_digits = 3, decimal_places=2)
    categorias = serializers.CharField(source = 'evento.categorias')
    responsable = serializers.CharField(source = 'evento.responsable')

    class Meta:
        model = FormacionIntegral
        fields = ('id',
                  'nombre',  
                  'matricula',
                  'asistencia',
                  'evento',
                  'alumno',
                  'created',
                  'modified',
                  'tituloEvento',
                  'unidadResponsable',  
                  'tituloEvento',
                  'descripcionEvento',
                  'eventoDedicadoA',
                  'fechaEvento',
                  'inicioEvento',
                  'finEvento',
                  'sede',
                  'cupo',
                  'descripcion',
                  'creditos',
                  'categorias',
                  'responsable'
                  )
        
        #fields = '__all__'