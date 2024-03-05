from rest_framework import serializers 
from .models import FormacionIntegral
from Alumnos.models import Oalumno
from eventos.models import eventosSubirevidenciasAlumno
 
 
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
    flayer = serializers.ImageField(source='evento.flayer')
    #Calendario
    
    fechaInicio = serializers.DateField(source = 'evento.fechaInicio')
    fechaFin = serializers.DateField(source = 'evento.fechaFin')
    inicioEvento = serializers.TimeField(source = 'evento.inicioEvento')
    finEvento = serializers.TimeField(source = 'evento.finEvento')
    sede = serializers.CharField(source = 'evento.sede')
    cupo = serializers.IntegerField(source = 'evento.cupo')
    descripcion = serializers.CharField(source = 'evento.descripcion')
    #Creditos
    creditos = serializers.DecimalField(source = 'evento.creditos', max_digits = 3, decimal_places=2)
    categorias = serializers.CharField(source = 'evento.categorias')
    responsable = serializers.CharField(source = 'evento.responsable')
    evidencia = serializers.SerializerMethodField()
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
                  'fechaInicio', 
                  'fechaFin',
                  'inicioEvento',
                  'finEvento',
                  'sede',
                  'cupo',
                  'descripcion',
                  'creditos',
                  'categorias',
                  'responsable', 
                  'evidencia', 
                  'flayer',
                  )
        
    def get_evidencia(self, obj): 
        evidencia = eventosSubirevidenciasAlumno.objects.filter(evento = obj.evento, cve_alumno = obj.matricula)
        if evidencia.exists(): 
            return True
        else: 
            return False

        
        #fields = '__all__'

