from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
from rest_framework import status

from Alumnos.Authentification import JWTAuthentication, create_access_token, create_refresh_token, decode_refresh_token

from .models import Alumnos
from .serializers import AlumnosSerializer, CoordinatorAlumnoSerializer

from .models import Oalumno
from .models import Oescuela
from .models import Omov_alumno, CustomUser, UserToken
from .serializers import oalumnoSerializer, omov_alumnoSerializer, UserSerializer

from rest_framework import generics
from allauth.socialaccount.providers.oauth2.views import OAuth2View

from rest_framework.views import APIView
from rest_framework import exceptions
import datetime

from google.oauth2 import id_token
from google.auth.transport.requests import Request as GoogleRequest
from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from allauth.socialaccount.models import SocialToken, SocialApp
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib.auth import authenticate, login
from google.oauth2 import id_token


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
    # API endpoint that returns a single customer by pk.
    queryset = Oalumno.objects.all()
    serializer_class = oalumnoSerializer

class MovAlumno(generics.ListAPIView): 
    queryset = Omov_alumno.objects.filter(cve_escuela__in = ['1820'], cve_ciclo = '790')[:100]
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
        cve_escuela_usuario = user.cve_escuela
        print(cve_escuela_usuario)

        queryset = Omov_alumno.objects.filter(cve_escuela=cve_escuela_usuario)[:200]
        return queryset




