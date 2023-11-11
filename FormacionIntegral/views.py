from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
import openpyxl
from .models import FormacionIntegral
from .serializers import FormacionInSerializer, FormacionInEventoSerializer
from rest_framework.decorators import APIView

from rest_framework import generics
import django_filters.rest_framework

class FormacionInCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = FormacionIntegral.objects.all(),
    serializer_class = FormacionInSerializer


class FormacionInList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = FormacionIntegral.objects.all()
    serializer_class = FormacionInSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['evento_id', 'matricula', 'alumno_id']


 
class FormacionInEventosList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = FormacionIntegral.objects.all()
    serializer_class = FormacionInEventoSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['evento_id', 'matricula', 'alumno_id']

...
class FormacionInDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = FormacionIntegral.objects.all()
    serializer_class = FormacionInSerializer

    ...
class FormacionInUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = FormacionIntegral.objects.all()
    serializer_class = FormacionInSerializer

class FormacionInDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = FormacionIntegral.objects.all()
    serializer_class = FormacionInSerializer


class generate_Excel(APIView): 
    def get(self, request, evento_id): 
        evento = get_object_or_404(FormacionIntegral, id=evento_id)

        alumno_evento = FormacionIntegral.objects.filter(evento_id=evento_id)

        wb = openpyxl.Workbook()
        ws = wb.active

        ws.append([
            "Nombre", "Matricula", "Asistencia",
             "Creditos"
        ])



        for alumno in alumno_evento: 
            serializer = FormacionInEventoSerializer(alumno)

            if serializer.data['asistencia'] == 0: 
                asistencia_value = "Falta"
            elif serializer.data['asistencia'] == 1: 
                asistencia_value = "Asistencia"
            else: 
                asistencia_value = "Pendiente"

            creditos_value = serializer.data['creditos'] if serializer.data['asistencia'] == 1 else None

            ws.append([
                serializer.data['nombre'],
                serializer.data['matricula'], 
                asistencia_value,
                creditos_value, 
                
            ])

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename=reporte_evento_{evento_id}.xlsx'
        wb.save(response)

        return response
