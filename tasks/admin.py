from django.contrib import admin
from .models import Doctor
from .models import Paciente
from .models import Cita

class PacienteAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )
    
class CitaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Cita, CitaAdmin)