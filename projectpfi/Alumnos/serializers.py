from rest_framework import serializers 
from .models import Alumnos, Oalumno, Omov_alumno, Oescuela, Ocarrera, CustomUser
from rest_framework.serializers import ModelSerializer

 
class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = ('id',
                  'nombres',  
                  'apellidos',
                  'matricula',
                  'carrera',                  
                  'semestre',
                  'correo',
                  'img',
                  'created',
                  'modified')
        
        

class oalumnoSerializer(serializers.ModelSerializer):  
    class Meta: 
        model = Oalumno
        fields = ('cve_alumno', 
                  'nombre', 
                  'paterno', 
                  'materno',
                  )
        
    

class omov_alumnoSerializer(serializers.ModelSerializer):     
    alumno = serializers.SerializerMethodField()
    desc_carrera = serializers.SerializerMethodField()
 
    class Meta: 
        model = Omov_alumno
        fields = ('cve_escuela', 
                  'semestre', 
                  'alumno', 
                  'cve_alumno', 
                  'desc_carrera', 
                  'object')
        
    def get_alumno(self, obj):
        nombre = {}
        alumno = Oalumno.objects.filter(cve_alumno = obj.cve_alumno).first()
        nombre.update({'nombre': alumno.nombre})
        nombre.update({'paterno': alumno.paterno})
        nombre.update({'materno': alumno.materno})
        return nombre 
        
    def get_desc_carrera(self, obj):
        desc_carrera = Ocarrera.objects.filter(cve_carrera = obj.cve_carrera).first()
        return desc_carrera.desc_carrera

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validate_data): 
        password = validate_data.pop('password', None)
        instance = self.Meta.model(**validate_data)
        if password is not None: 
            instance.set_password(password)
        instance.save()
        return instance