from django.db import models
from django.utils.functional import cached_property


class Persona(models.Model):
    genero_choice = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    ci = models.CharField(max_length=11, unique=True)
    direccion = models.CharField(max_length=200)
    numero_telefono = models.CharField(max_length=11)
    reparto = models.CharField(max_length=30)
    municipio = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    genero = models.CharField(max_length=1, choices=genero_choice)

    def edad(self):
        return 18

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

    class Meta:
        abstract = True


class Cientifico(models.Model):
    categoria_cientifica_choices = [
        ('máster', 'máster'),
        ('doctor', 'doctor'),
    ]
    categoria_cientifica = models.CharField(max_length=100, choices=categoria_cientifica_choices, null=True, blank=True)

    class Meta:
        abstract = True


class Grado(models.Model):
    grado_choice = [
        ('7', '7mo'),
        ('8', '8vo'),
        ('9', '9no')
    ]
    nombre = models.CharField(max_length=1, choices=grado_choice, primary_key=True)

    def __str__(self):
        return self.nombre


class Asignatura(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Grupo(models.Model):
    numero_grupo = models.CharField(max_length=30)

    def __str__(self):
        return self.numero_grupo


class Profesor(Persona, Cientifico):
    categoria_docente_choices = [
        ('Profesor Titular', 'Profesor Titular'),
        ('Profesor Auxiliar', 'Profesor Auxiliar'),
        ('Asistente', 'Asistente'),
        ('Instructor', 'Instructor'),
        ('Instructor Auxiliar', 'Instructor Auxiliar'),
        ('Auxiliar Técnico de la Docencia', 'Auxiliar Técnico de la Docencia'),
        ('Profesor de Mérito', 'Profesor de Mérito'),
        ('Profesor Invitado', 'Profesor Invitado')
    ]
    categoria_docente = models.CharField(max_length=100, choices=categoria_docente_choices, null=True, blank=True)
    grupos = models.ManyToManyField(Grupo)
    asignatura = models.ManyToManyField(Asignatura)


class ProfesorGuia(Profesor):
    grupo = models.OneToOneField(Grupo, on_delete=models.CASCADE)
    profesor = models.OneToOneField(Profesor, on_delete=models.CASCADE, related_name='pg_profesor')


class Estudiante(Persona):
    nombre_apellido_padre = models.CharField(max_length=150)
    nombre_apellido_madre = models.CharField(max_length=150)
    grado = models.ForeignKey(Grado, on_delete=models.DO_NOTHING, null=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True)


class Nota(models.Model):
    tipo_choice = [
        ('ES', 'Evaluación Sistemática'),
        ('EP', 'Evaluación Parcial'),
        ('EF', 'Evaluación Final')
    ]
    valor = models.IntegerField()
    tipo = models.CharField(max_length=100, choices=tipo_choice)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.RESTRICT)


class Curso(models.Model):
    nombre = models.CharField(max_length=20, primary_key=True, unique=True)

    def __str__(self):
        return self.nombre


class ProgramaDeEstudio(models.Model):
    asignatura = models.ManyToManyField(Asignatura)
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT)
    grado = models.ForeignKey(Grado, on_delete=models.RESTRICT)
    archivo = models.FileField()

    def __str__(self):
        return f'{self.curso} {self.grado}'


