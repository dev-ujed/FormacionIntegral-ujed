from django.conf.urls import url 
from eventos import views 
 
from django.urls import include, path
from .views import *
from eventos import seeders
from django.views.generic import TemplateView

#urlpatterns = [ 
#  url(r'^api/eventos$', views.eventos_list),
 #   url(r'^api/eventos/(?P<pk>[0-9]+)$', views.eventos_detail)
    #url(r'^api/eventos/published$', views.eventos_list_fechaEvento)
#]

urlpatterns = [
    path('create/', eventosCreate.as_view(), name='crear-evento'),
    path('create/calendario/', calendarioCreate.as_view(), name='crear-calendario'),
    path('', eventosList.as_view()),
    path('calendario', calendarioList.as_view()),
    path('<int:pk>/', eventosDetail.as_view(), name='retrieve-evento'),
    path('update/<int:pk>/', eventosUpdate.as_view(), name='actualizar-evento'),
    #path('put/<int:pk>/', eventosUpdate.as_view(), name='actualizar-evento'),
    path('delete/<int:pk>/', eventosDelete.as_view(), name='eliminar-evento'),
    path('create/evidencia', evidencias.as_view(), name='crear-evidencia'),
    path('update/evidencia/<int:pk>/', evidenciasUpdate.as_view(), name='actualizar-evidencia'),
    path('evidencia',evidenciasList.as_view(), name='retrieve-evidencia'),
    path('run-seeders/', view=seeders.SeederModel, name='seeder-model'),
    
    #Catalogos
    path('clasificacion_eve', ClasificacionEventosList.as_view()),
    path('categorias1_eve', Categorias1List.as_view()),
    path('categorias2_eve', Categorias2List.as_view()),
    path('categoriasArte_eve', CategoriasArteList.as_view()),

    path('matricula-evidencia/<str:matricula>/', evidenciaPorMatricula.as_view()),
    path('escuela', escuela.as_view()),
    path('clave/<str:cveUnidadResponsable>/', eventoPorUnidad.as_view()),
    path('ciclos/<str:cve_ciclo>/', eventoPorCiclo.as_view())
]
