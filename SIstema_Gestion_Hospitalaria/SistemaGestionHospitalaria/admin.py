from django.contrib import admin
from .models import Doctor, Paciente, Enfermero, CitasMedicas, ExpedienteMedico

admin.site.register(Doctor)
admin.site.register(Enfermero)
admin.site.register(Paciente)
admin.site.register(CitasMedicas)
admin.site.register(ExpedienteMedico)
