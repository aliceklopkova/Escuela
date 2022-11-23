from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.contrib.auth.models import User


class Persona(models.Model):
    genero_choice = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, null=True, blank=True)
    fecha_nacimiento = models.DateField()
    ci = models.CharField(max_length=11, unique=True)
    direccion = models.CharField(max_length=200)
    numero_telefono = models.CharField(max_length=11)
    reparto = models.CharField(max_length=30)
    municipio = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    genero = models.CharField(max_length=1, choices=genero_choice)

    @cached_property
    def edad(self):
        if self.fecha_nacimiento:
            today = timezone.now()
            return today.year - self.fecha_nacimiento.year - (
                    (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return None

    def __str__(self):
        return f'{self.nombre} {self.primer_apellido}'

    class Meta:
        abstract = True


class Cientifico(models.Model):
    grado_academico_choices = [
        ('universitario', 'Universitario'),
        ('master', 'Máster en Ciencias'),
        ('doctor', 'Doctor en Ciencias'),
    ]
    grado_academico = models.CharField(max_length=100, choices=grado_academico_choices, null=True, blank=True)

    class Meta:
        abstract = True


class Grado(models.Model):
    GRADOS = {
        '7': '7mo',
        '8': '8vo',
        '9': '9no'
    }
    grado_choice = [
        ('7', '7mo'),
        ('8', '8vo'),
        ('9', '9no')
    ]
    nombre = models.CharField(max_length=1, choices=grado_choice)

    def __str__(self):
        return self.GRADOS[self.nombre]


class Asignatura(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Grupo(models.Model):
    numero_grupo = models.CharField(max_length=30)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.grado.__str__()} {self.numero_grupo}'

    class Meta:
        unique_together = ('numero_grupo', 'grado')


class Profesor(Persona, Cientifico):
    categoria_docente_choices = [
        ('profesor_titular', 'Profesor Titular'),
        ('profesor_auxiliar', 'Profesor Auxiliar'),
        ('asistente', 'Asistente'),
        ('instructor', 'Instructor'),
        ('instructor_auxiliar', 'Instructor Auxiliar'),
        ('auxiliar_tecnico', 'Auxiliar Técnico de la Docencia'),
        ('profesor_de_merito', 'Profesor de Mérito'),
        ('profesor_invitado', 'Profesor Invitado')
    ]
    categoria_docente = models.CharField(max_length=100, choices=categoria_docente_choices, null=True, blank=True)
    grupos = models.ManyToManyField(Grupo)
    asignaturas = models.ManyToManyField(Asignatura)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)


class ProfesorGuia(models.Model):
    grupo = models.OneToOneField(Grupo, on_delete=models.CASCADE)
    profesor = models.OneToOneField(Profesor, on_delete=models.CASCADE, related_name='pg_profesor')

    def __str__(self):
        return self.profesor.__str__()


class Estudiante(Persona):
    nombre_apellido_padre = models.CharField(max_length=150)
    nombre_apellido_madre = models.CharField(max_length=150)
    grado = models.ForeignKey(Grado, on_delete=models.DO_NOTHING, null=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True)


class Nota(models.Model):
    tipo_choice = [
        ('es', 'Evaluación Sistemática'),
        ('ep', 'Evaluación Parcial'),
        ('ef', 'Evaluación Final')
    ]
    valor = models.IntegerField()
    tipo = models.CharField(max_length=100, choices=tipo_choice)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.RESTRICT)

    def __str__(self):
        return self.valor


class Curso(models.Model):
    nombre = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre


class ProgramaDeEstudio(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.RESTRICT)
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT)
    grado = models.ForeignKey(Grado, on_delete=models.RESTRICT)
    horas_clases = models.IntegerField(null=True)
    frecuencia = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.curso} {self.grado}'

    class Meta:
        unique_together = ('asignatura', 'curso', 'grado')
