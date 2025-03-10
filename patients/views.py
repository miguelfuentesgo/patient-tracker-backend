from rest_framework import viewsets
from .models import Patient, Log
from .serializers import PatientSerializer, LogSerializer
import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer



@api_view(['GET'])
def validate_patient(request, email):
    url = f'https://randomuser.me/api/?email={email}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if len(data.get("results", [])) > 0:
            return JsonResponse({"exists": True, "data": data["results"][0]})
        else:
            return JsonResponse({"exists": False})
    else:
        return JsonResponse({"error": "Connection to api is no possible"}, status=500)
