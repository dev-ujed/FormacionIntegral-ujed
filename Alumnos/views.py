from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from django.db.models import OuterRef, Subquery, Max
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
from rest_framework import status

from Alumnos.Authentification import JWTAuthentication, create_access_token, create_refresh_token, decode_refresh_token

from .models import Alumnos
from .serializers import AlumnosSerializer, CoordinatorAlumnoSerializer

from .models import Oalumno
from .models import Oescuela
from .models import Omov_alumno, CustomUser, UserToken
from .models import Ociclo_carrera
from .serializers import oalumnoSerializer, omov_alumnoSerializer, UserSerializer, ocicloSerializer

from rest_framework import generics


from rest_framework.views import APIView
from rest_framework import exceptions
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import openpyxl

from eventos.models import Oparametros_dtd


class AlumnosCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Alumnos.objects.all(),
    serializer_class = AlumnosSerializer


class AlumnosList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Alumnos.objects.all()
    serializer_class = AlumnosSerializer

class AlumnosDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Alumnos.objects.all()
    serializer_class = AlumnosSerializer



class AlumnosUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Alumnos.objects.all()
    serializer_class = AlumnosSerializer


class AlumnosDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Alumnos.objects.all()
    serializer_class = AlumnosSerializer

class AlumnosListView(generics.ListAPIView): 
    queryset = Oalumno.objects.all()[:1000]
    serializer_class = oalumnoSerializer

class AlumnosDetailOracle(generics.RetrieveAPIView):
    serializer_class = oalumnoSerializer
    lookup_field = 'cve_alumno'
    def get_queryset(self):
        # Obtener el ciclo actual desde la tabla Oparametros_dtd
        ciclo_actual = Oparametros_dtd.objects.get(id=61).valor
        # Subconsulta para obtener la última fecha_mov para cada matrícula
        latest_movements = Omov_alumno.objects.filter(
            cve_ciclo=ciclo_actual,
            cve_alumno=OuterRef('cve_alumno')  # Vincula la matrícula externa
        ).order_by('fecha_mov').values('fecha_mov')[:1]
        # Filtrar registros con el ciclo actual y la última fecha_mov por matrícula
        filtered_query = Omov_alumno.objects.filter(
            cve_ciclo=ciclo_actual,
            fecha_mov=Subquery(latest_movements)  # Vincula con la subconsulta
        )
        return filtered_query

class MovAlumno(generics.ListAPIView): 
    queryset = Omov_alumno.objects.filter()[:1000]
    serializer_class = omov_alumnoSerializer
    
    def get_object(self):
        return self.request.user 

class MovAlumnoDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Omov_alumno.objects.all()
    serializer_class = omov_alumnoSerializer

class ReggisterApiView(APIView):
    def post(self, request):
        data = request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('La contraseña no concuerda')

        serializer = UserSerializer(data=data)
        serializer.is_valid() 

        

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)  

        serializer.save()
        return Response(serializer.data, status=201)
    

class LoginApiView(APIView): 
    def post(self, request): 
        email = request.data['email']
        password = request.data['password']

        if not email.endswith('@ujed.mx'): 
            raise exceptions.AuthenticationFailed("Only users with @ujed.mx can login")

        user = CustomUser.objects.filter(email=email).first()

        if user is None: 
            raise exceptions.AuthenticationFailed('Authentication failed')
        
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Invalid credentials')
        
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        UserToken.objects.create(
            user_id = user.id,
            token = refresh_token, 
            expired_at = datetime.datetime.utcnow() + datetime.timedelta(days=7)
        )
        
        response = Response()
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        response.data = {
            'token' : access_token
        }

        return response
  
class UserApiView(APIView): 
    authentication_classes = [JWTAuthentication]

    def get(self, request): 
        return Response(UserSerializer(request.user).data)
 
class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        id = decode_refresh_token(refresh_token)

        if not UserToken.objects.filter(
            user_id = id, 
            token = refresh_token, 
            expired_at__gt=datetime.datetime.now(tz=datetime.timezone.utc)
        ).exists(): 
            raise exceptions.AuthenticationFailed('unaunthenticated')

        access_token = create_access_token(id)

        return Response({
            'token': access_token
        })
    

class LogoutApiView(APIView):
    def post(self, request):

        refresh_token = request.COOKIES.get('refresh_token')

        UserToken.objects.filter(token = refresh_token).delete

        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data = {
            'message': 'success'
        }

        return response 
    
class CoordinatorAlumnosListView(generics.ListAPIView):
    serializer_class = omov_alumnoSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        ciclos = self.request.GET.get('cve_ciclo')
        print("Valor de cve_ciclo:", ciclos)
        queryset = Omov_alumno.objects.filter(
            cve_ciclo=ciclos
        )[:1000]
        #print("Consulta SQL:", queryset.query)
        return queryset

