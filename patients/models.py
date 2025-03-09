from django.db import models

from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    disease = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Log(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="logs")
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True) 
    note = models.TextField()

    def __str__(self):
        return f"Logginf of {self.patient.name} - {self.date.strftime('%Y-%m-%d')}"
