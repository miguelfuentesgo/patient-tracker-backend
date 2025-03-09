from rest_framework import serializers
from .models import Patient, Log

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    logs = LogSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'
