from django .db                     import models
from django .db    .models.deletion import CASCADE
from Alumnos.models                 import Alumnos , Oalumno
from django .utils                  import timezone

# Create your models here. 
class clasifi_cat(  models.Model                     ):
          text        = models.CharField(max_length = 100)

class catalogo_categorias(  models.Model                                                ):
          text                = models.CharField (max_length = 100                          )
          objetivo            = models.TextField (null=True                                 )
          clasificacion       = models.ForeignKey(clasifi_cat, on_delete=CASCADE, null= True)

class catalogo_categorias2(  models.Model                                                        ):
          text                 = models.CharField (max_length = 100                                  )
          catalogo             = models.ForeignKey(catalogo_categorias, on_delete=CASCADE, null= True)

class arte_categorias(  models.Model                                                         ):
          text            = models.CharField (max_length = 100                                   )
          categoria       = models.ForeignKey(catalogo_categorias2, on_delete=CASCADE, null= True)

class Oparametros_dtd(models.Model):
      id                  = models.IntegerField(primary_key=True)
      valor               = models.CharField(max_length=4000)

      class Meta:
            managed       = False
            db_table      = '"API_ESCOLAR"."PARAMETROS_DTD"'
            app_label     = 'desarrollo'


class eventos(models.Model):
    #     Descripción
      unidadResponsable = models.CharField('unidadResponsable', max_length=150, blank=False,default='')
      cveUnidadResponsable = models.CharField('cveUnidadResponsable', max_length=150, blank=False, default='')
      tituloEvento      = models.CharField('tituloEvento', max_length=200,blank=False,default='')
      descripcionEvento = models.TextField('descripcionEvento')
      eventoDedicadoA   = models.CharField('eventoDedicadoA', max_length=200)
      flayer            = models.ImageField(upload_to='Eventos/images', null= True)
    #     Calendario
      #     fechaEvento       = models.DateField('fechaEvento', default=timezone.now)
      inicioEvento      = models.TimeField('inicioEvento', null=True, blank=True)
      finEvento         = models.TimeField('finEvento', null=True, blank=True)
      sede              = models.CharField('sede', max_length=150)
      cupo              = models.IntegerField('cupo')
      descripcion       = models.TextField('descripcion')
    #     Créditos
      creditos          = models.DecimalField('creditos', max_digits = 3,decimal_places=2)
      categorias        = models.ForeignKey(clasifi_cat, on_delete=models.CASCADE, null = True, related_name='categorias')
      subCategoria1     = models.ForeignKey(catalogo_categorias, on_delete=models.CASCADE, null= True, related_name='categorias1')
      subCategoria2     = models.ForeignKey(catalogo_categorias2, on_delete=models.CASCADE, null= True, related_name='categorias2')
      subCategoriaArte  = models.ForeignKey(arte_categorias, on_delete=models.CASCADE, null= True, related_name='categoriasArte')
    #     Crear             eventos responsable
      responsable       = models.CharField('responsable', max_length=200)
    #     fechas
      fechaInicio       = models.DateField('fechaInicio')
      fechaFin          = models.DateField('fechaFin', null=True, blank=True)
      horas_totales     = models.IntegerField('horas_totales', blank=True, null=True)  
      contacto          =  models.CharField('contacto', max_length=100, blank=True, null=True)
      cve_ciclo         = models.CharField('cve_ciclo', blank=True, null=True, max_length=100)
      creacionEvento    = models.DateTimeField('creacionEvento', auto_now_add = True)
    
#     modelo            para   el    modulo calendario de eventos
class eventosCalendario(models.Model):

    name    = models.CharField ('name'   , max_length=200           )
    color   = models.CharField ('color'  , max_length=100           )
    start   = models.CharField ('start'  , max_length=200           )
    end     = models.CharField ('end'    , max_length=200           )
    details = models.CharField ('details', max_length=250           )
    evento  = models.ForeignKey(eventos  , on_delete =models.CASCADE)

class eventosSubirevidenciasAlumno(  models.Model                                          ):
          img                          = models.FileField(upload_to='EvidenciasAlumnos/images')
          evento                       = models.ForeignKey(eventos, on_delete=models.CASCADE   )
          cve_alumno                   = models.CharField ("cve_alumno", max_length=9          )

# class oescuela(models.Model):
#       cve_escuela = models.CharField('cve_escuela', max_length=150, blank=False,default='')
#       desc_escuela = models.CharField('desc_escuela', max_length=150, blank=False,default='')

#       class Meta:
#             managed = False
#             db_table = 'ESCUELA'
#             app_label = 'desarrollo'