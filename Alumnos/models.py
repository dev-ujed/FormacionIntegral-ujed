from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class Alumnos(models.Model):
    nombres = models.CharField('nombres', max_length=80)
    apellidos = models.CharField('apellidos', max_length=80)
    matricula = models.CharField('matricula', max_length=50)
    carrera = models.CharField('carrera', max_length=50)
    # semestre = models.IntegerField('semestre') 
    correo = models.EmailField('correo', max_length=50)
    contraseña = models.CharField('contraseña', max_length=50)
    img = models.ImageField(upload_to='Alumnos/images')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Omov_alumno(models.Model):
    cve_alumno              = models.CharField(primary_key=True, max_length=9)
    cve_ciclo               = models.PositiveSmallIntegerField()
    cve_estatus             = models.PositiveSmallIntegerField()
    cve_carrera             = models.CharField(max_length=8)
    cve_escuela             = models.CharField(max_length=8)
    semestre                = models.PositiveSmallIntegerField()
    cve_plan                = models.CharField(max_length=5)
    no_incluir              = models.CharField(max_length=1)
    fecha_mov               = models.DateTimeField()
    registro                = models.IntegerField()
    alumno_id               = models.IntegerField()
    mov_alumno_id           = models.IntegerField()
    carrera_id              = models.IntegerField()
    ciclo_id                = models.IntegerField()
    escuela_id              = models.IntegerField()
    plan_estudio_id         = models.IntegerField()
    estatus_id              = models.IntegerField()
    f_reg                   = models.DateTimeField()
    mod_tit_id              = models.IntegerField()
    veredicto_examen_id     = models.IntegerField()
    class Meta:
        managed     = False
        db_table    = 'MOV_ALUMNO'
        app_label   = 'desarrollo'


class Oescuela(models.Model):
    cve_escuela             = models.CharField(primary_key=True, max_length=8)
    escuela_imprime         = models.CharField(max_length=80)
    desc_completo           = models.CharField(max_length=100)
    desc_escuela            = models.CharField(max_length=40)
    ubicacion               = models.CharField(max_length=30)
    class Meta: #Metadatos adicionales
        #La tabla Escuela debe de existir en la base de datos
        managed     = False
        db_table    = 'ESCUELA'
        app_label   = 'desarrollo'


class Oalumno(models.Model):
    cve_alumno              = models.CharField(primary_key=True, max_length=9)
    nombre                  = models.CharField(null=False, max_length=35)
    paterno                 = models.CharField(null=False, max_length=20)
    materno                 = models.CharField(null=True, max_length=20)
    sexo                    = models.CharField(max_length=9)
    f_nacimiento            = models.DateField(null=True)
    curp                    = models.CharField(max_length=18)
    rfc                     = models.CharField(null=True, max_length=13)
    cve_edo_nac             = models.CharField(max_length=2)
    cve_mun_nac             = models.CharField(max_length=5)
    correo                  = models.EmailField(null=True, max_length=50)
    correo_institucional    = models.CharField(max_length=100)
    trabaja                 = models.CharField(max_length=1)
    est_civil               = models.CharField(max_length=7)
    comunidad_indigena      = models.CharField(max_length=60)
    pertenece_comunidad     = models.CharField(max_length=1)
    apoyo                   = models.CharField(max_length=1)
    credencial              = models.CharField(max_length=1)
    discapacidad            = models.IntegerField()
    num_cred                = models.CharField(max_length=20)
    calle                   = models.CharField(max_length=30)
    colonia                 = models.CharField(max_length=30)
    telefono                = models.CharField(max_length=15)
    codigo                  = models.CharField(max_length=10)
    ciudad                  = models.CharField(max_length=50)
    tel_cel                 = models.CharField(max_length=15)
    tel_ofi                 = models.CharField(max_length=15)
    esc_procedencia         = models.CharField(max_length=45)
    cve_procedencia         = models.IntegerField()
    cve_usuario             = models.CharField(max_length=32)
    extranjero              = models.CharField(max_length=1)
    cve_edo_pro             = models.CharField(max_length=2)
    cve_mun_pro             = models.CharField(max_length=5)
    f_ing_inst              = models.DateField(null=False)
    cer_sec                 = models.CharField(max_length=1)
    cer_pre                 = models.CharField(max_length=1)
    cta_bc                  = models.CharField(max_length=1)
    
  
    class Meta:  
        managed = False
        db_table = 'ALUMNO'
        app_label = 'desarrollo'


class Ocarrera(models.Model):
	cve_carrera 			= models.CharField(primary_key=True, max_length=8)
	carrera_imprime 		= models.CharField(max_length=100)
	desc_carrera 			= models.CharField(max_length=60)
	cve_escuela 			= models.CharField(max_length=8)
	cve_nivel				= models.CharField(max_length=8)
	desc_carrera_prof		= models.CharField(max_length=100)
	desc_carrera_mujer		= models.CharField(max_length=100)
	desc_carrera_hombre		= models.CharField(max_length=100)
	diploma_grado			= models.CharField(max_length=100)
	desc_certificado		= models.CharField(max_length=2)
	acta_examen				= models.CharField(max_length=30)
	activa					= models.CharField(max_length=30)

	class Meta:
		managed 	= False 
		db_table 	= 'CARRERA'
		app_label 	= 'desarrollo'
          

class Ociclo_carrera(models.Model):
	cve_ciclo 				= models.PositiveSmallIntegerField(primary_key=True)
	cve_carrera 			= models.CharField(max_length=8)
	estatus_ciclo 			= models.CharField(max_length=1)
	cve_escuela 			= models.CharField(max_length=8)
	cve_plan 				= models.CharField(max_length=3)
	cve_ciclo_sig			= models.PositiveSmallIntegerField()
	fecha_carta				= models.DateField()

	class Meta:
		managed 	= False
		db_table 	= 'CICLO_CARRERA'
		app_label 	= 'desarrollo'

class Oparametros(models.Model):
	cve_parametro	= models.IntegerField(primary_key=True)
	valor			= models.CharField(max_length=4000)

	class Meta:
		managed		= False
		db_table	= '"DESARROLLO"."PARAMETROS"'
		app_label	= 'desarrollo'

class CustomUser(AbstractUser):
    email = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    username = None 
 
    is_coordinator = models.BooleanField(default=False)
    cve_escuela = models.CharField(max_length=8, null=True)    
    cve_carrera = models.CharField(max_length=300, null=True)

    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class UserToken(models.Model):
     user_id = models.IntegerField()
     token = models.CharField(max_length=255)
     created_at = models.DateTimeField(auto_now_add=True)
     expired_at = models.DateTimeField()


