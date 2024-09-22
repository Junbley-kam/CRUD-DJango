from django.db import models
from django.contrib.auth.models import User

# Modelo para Doctor
class Doctor(models.Model):
    nombre = models.CharField(max_length=200)
    especialidad = models.TextField(blank=True)
    horarios_del_profesional = models.CharField(max_length=200, blank=True)
    consultorio = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre + '- by ' + self.user.username

# Modelo para Paciente
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True) # Fecha y hora de creacion de la tarea
    datecompleted = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre + '- by ' + self.user.username
    
# Modelo para Cita
class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    motivo = models.TextField()
    created = models.DateTimeField(auto_now_add=True) # Fecha y hora de creacion de la tarea
    datecompleted = models.DateTimeField(null=True)