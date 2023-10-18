from rest_framework import serializers 
from .models import Alumnos, Oalumno, Omov_alumno, Oescuela, Ocarrera, CustomUser, Ociclo_carrera, Oparametros
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

class ocicloSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = Ociclo_carrera
        fields = ('cve_escuela', 
                  'estatus_ciclo', 
                  'cve_carrera', 
                  'cve_ciclo' 
                    )
    

class oparametroSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Oparametros
        fields = ('cve_parametro', 
                  'valor')

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
                  'cve_ciclo', 
                  'cve_carrera'
                  )
        
    def get_alumno(self, obj): 
        nombre = {}
        alumno = Oalumno.objects.filter(cve_alumno = obj.cve_alumno).first()
        nombre.update({'nombre': alumno.nombre})
        nombre.update({'paterno': alumno.paterno})
        nombre.update({'materno': alumno.materno})
        return nombre 
    
    def get_desc_carrera(self, obj): 
        desc_carrera = Ocarrera.objects.filter(cve_carrera = obj.cve_carrera).last()
        return desc_carrera.desc_carrera
        
    


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'email', 'password', 'is_coordinator', 'cve_escuela']
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
    
class CoordinatorAlumnoSerializer(serializers.ModelSerializer): 
    alumno = serializers.SerializerMethodField()
    desc_carrera = serializers.SerializerMethodField()
    

    class Meta: 
        model = Omov_alumno
        fields = ['cve_escuela', 'semestre', 'alumno', 'cve_alumno', 'desc_carrera']

        def get_alumno(self, obj): 
            alumno = Oalumno.objects.filter(cve_alumno = obj.cve_alumno).first()
            return{
                'nombre': alumno.nombre, 
                'paterno': alumno.paterno, 
                'materno': alumno.materno
            }
        
        def get_desc_carrera(self,obj): 
            desc_carrera = Ocarrera.objects.filter(cve_carrera=obj.cve_carrera).first()
            return desc_carrera.desc_carrera
        
      
