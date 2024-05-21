from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    #id = models.CharField(max_length=100)
    direccion = models.CharField(max_length= 100)
    class Meta:
        abstract = True
    def __str__(self):
        return self.nombre

class Especialidad(models.TextChoices):
    PEDIATRIA = 'Pediatría'
    CARDIOLOGIA = 'Cardiología'
    MEDICINA_GENERAL = 'Medicina General'
    TRAUMATOLOGIA = 'Traumatología'
    PSIQUIATRIA = 'Psiquiatría'
    ONCOLOGIA = 'Oncología'

class Doctor(Persona):
    especialidad = models.CharField(max_length=50, choices=Especialidad.choices)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"
class Enfermero(Persona):
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()
    class Meta:
        verbose_name = "Enfermero"
        verbose_name_plural = "Enfermeros"
class Paciente(Persona):
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
class Estado(models.TextChoices):
    PENDIENTE = 'Pendiente'
    REALIZADA = 'Realizada'
    CANCELADA = 'Cancelada'

class GestionCitas(models.Model):
    def programarCitas(self, fecha, tipo_cita, paciente, doctor):
        return CitasMedicas.objects.create(
            fecha=fecha,
            tipo_cita=tipo_cita,
            paciente=paciente,
            doctor=doctor,
            estado=Estado.PENDIENTE
        )

class CitasMedicas(models.Model):
    fecha = models.DateTimeField()
    tipo_cita = models.CharField(max_length=50)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=Estado.choices)

class ExpedienteMedico(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    diagnosticos = models.TextField()
    def __str__(self):
        return f"Expediente de {self.paciente.nombre}"

