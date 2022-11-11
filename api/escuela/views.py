from rest_framework import viewsets
from django_auto_prefetching import AutoPrefetchViewSetMixin
from .models import Estudiante, PersonalNoDocente, Nota, Grupo, Grado, Curso, Asignatura, ProgramaDeEstudio, Profesor, \
    ProfesorGuia
from .serializers import EstudianteSerializer, PersonalNoDocenteSerializer, CursoSerializer, AsignaturaSerializer, \
    ProfesorSerializer, ProfesorGuiaSerializer, GradoSerializer, ProgramaDeEstudioSerializer, NotaSerializer, \
    GrupoSerializer


class EstudianteViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    search_fields = ['nombre', 'apellidos', 'grupo', 'grado']
    filterset_fields = ['nombre', 'apellidos', 'grupo', 'grado', 'ci', 'reparto', 'municipio', 'provincia', 'genero']


class ProfesorViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer


class ProfesorGuiaViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ProfesorGuia.objects.all()
    serializer_class = ProfesorGuiaSerializer


class GrupoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer


class GradoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer


class AsignaturaViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer


class NotaViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class ProgramaDeEstudioViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ProgramaDeEstudio.objects.all()
    serializer_class = ProgramaDeEstudioSerializer


class PersonalNoDocenteViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = PersonalNoDocente.objects.all()
    serializer_class = PersonalNoDocenteSerializer
