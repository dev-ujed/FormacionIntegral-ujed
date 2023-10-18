from django.conf.urls import url 
from Alumnos import views 
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from .views import AlumnosCreate, AlumnosList, AlumnosDetail, AlumnosUpdate, AlumnosDelete, AlumnosListView,MovAlumno, ReggisterApiView, LoginApiView, UserApiView, RefreshAPIView, LogoutApiView, CoordinatorAlumnosListView, AlumnosDetailOracle

urlpatterns = [
    path('create/', AlumnosCreate.as_view(), name='crear-evento'),
    path('', AlumnosList.as_view()),
    path('<int:pk>/', AlumnosDetail.as_view(), name='retrieve-evento'),
    path('movalumno/<str:pk>/', AlumnosDetailOracle.as_view(), name='retrieve-evento'),
    path('update/<int:pk>/', AlumnosUpdate.as_view(), name='actualizar-evento'),
    path('delete/<int:pk>/', AlumnosDelete.as_view(), name='eliminar-evento'), 
    path('oalumnos/', AlumnosListView.as_view(), name='get_oalumnos'),
    path('movalumno/', MovAlumno.as_view(), name="get_movalumnos"),
    path('accounts/', include('allauth.urls')),
    path('register/', ReggisterApiView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('user/', UserApiView.as_view()), 
    path('refresh/', RefreshAPIView.as_view()), 
    path('logout/', LogoutApiView.as_view()), 
    path('get_coordinator', CoordinatorAlumnosListView.as_view()),  
      
]