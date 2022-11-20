from django_auto_prefetching import AutoPrefetchViewSetMixin
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Estudiante, Nota, Grupo, Grado, Curso, Asignatura, ProgramaDeEstudio, Profesor, \
    ProfesorGuia
from .serializers import EstudianteSerializer, CursoSerializer, AsignaturaSerializer, \
    ProfesorSerializer, ProfesorGuiaSerializer, GradoSerializer, ProgramaDeEstudioSerializer, NotaSerializer, \
    GrupoSerializer


class EstudianteViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    search_fields = ['^nombre', '^primer_apellido', '^segundo_apellido']
    filterset_fields = ['nombre', 'primer_apellido', 'segundo_apellido', 'grupo', 'grado', 'ci', 'reparto', 'municipio',
                        'provincia', 'genero']

    @action(detail=False, methods=["GET"], name="Get Filters", url_path="filters")
    def get_filters(self, request, *args, **kwargs):
        return Response(data={'filters': self.filterset_fields}, status=status.HTTP_200_OK)


class ProfesorViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    search_fields = ['^nombre', '^primer_apellido', '^segundo_apellido']
    filterset_fields = ['nombre', 'primer_apellido', 'segundo_apellido', 'ci', 'reparto', 'municipio',
                        'provincia', 'genero', 'categoria_docente', 'asignaturas']

    @action(detail=False, methods=["GET"], name="Get Filters", url_path="filters")
    def get_filters(self, request, *args, **kwargs):
        return Response(data={'filters': self.filterset_fields}, status=status.HTTP_200_OK)


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
