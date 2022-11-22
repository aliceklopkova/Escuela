from django.contrib.auth.models import User, Group, Permission
from django_auto_prefetching import AutoPrefetchViewSetMixin
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Estudiante, Nota, Grupo, Grado, Curso, Asignatura, ProgramaDeEstudio, Profesor, \
    ProfesorGuia
from .serializers import CursoSerializer, AsignaturaSerializer, ProfesorReadGuiaSerializer, ProfesorWriteGuiaSerializer, \
    GradoSerializer, ProgramaDeEstudioSerializer, GrupoReadSerializer, GrupoWriteSerializer, UserSerializer, \
    GroupSerializer, PermissionSerializer, ProfesorReadSerializer, ProfesorWriteSerializer, EstudianteWriteSerializer, \
    EstudianteReadSerializer, NotaReadSerializer, NotaWriteSerializer


def assign_serializer(obj, list_serializer, read_serializer, write_serializer):
    p = {
        'retrieve': read_serializer,
        'update': write_serializer,
        'create': write_serializer,
        'list': list_serializer,
        'partial_update': write_serializer,
    }
    if obj.action in p:
        return p[obj.action]
    return read_serializer


class UserViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class EstudianteViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Estudiante.objects.all()

    search_fields = ['^nombre', '^primer_apellido', '^segundo_apellido']
    filterset_fields = ['nombre', 'primer_apellido', 'segundo_apellido', 'grupo', 'grado', 'ci', 'reparto', 'municipio',
                        'provincia', 'genero']

    def get_serializer_class(self):
        return assign_serializer(self, EstudianteReadSerializer, EstudianteReadSerializer,
                                 EstudianteWriteSerializer)

    @action(detail=False, methods=["GET"], name="Get Filters", url_path="filters")
    def get_filters(self, request, *args, **kwargs):
        return Response(data={'filters': self.filterset_fields}, status=status.HTTP_200_OK)


class ProfesorViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Profesor.objects.all()

    search_fields = ['^nombre', '^primer_apellido', '^segundo_apellido']
    filterset_fields = ['nombre', 'primer_apellido', 'segundo_apellido', 'ci', 'reparto', 'municipio',
                        'provincia', 'genero', 'categoria_docente', 'asignaturas']

    def get_serializer_class(self):
        return assign_serializer(self, ProfesorReadSerializer, ProfesorReadSerializer,
                                 ProfesorWriteSerializer)

    @action(detail=False, methods=["GET"], name="Get Filters", url_path="filters")
    def get_filters(self, request, *args, **kwargs):
        return Response(data={'filters': self.filterset_fields}, status=status.HTTP_200_OK)


class ProfesorGuiaViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ProfesorGuia.objects.all()

    def get_serializer_class(self):
        return assign_serializer(self, ProfesorReadGuiaSerializer, ProfesorReadGuiaSerializer,
                                 ProfesorWriteGuiaSerializer)


class GrupoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Grupo.objects.all()

    def get_serializer_class(self):
        return assign_serializer(self, GrupoReadSerializer, GrupoReadSerializer, GrupoWriteSerializer)


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

    @action(detail=False, methods=["GET"], name="Get Filters", url_path="filters")
    def get_filters(self, request, *args, **kwargs):
        return Response(data={'filters': []}, status=status.HTTP_200_OK)


class NotaViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Nota.objects.all()
    search_fields = ['^estudiante__nombre', '^estudiante__primer_apellido', 'asignatura__nombre']
    filterset_fields = ['estudiante', 'asignatura', 'tipo']

    def get_serializer_class(self):
        return assign_serializer(self, NotaReadSerializer, NotaReadSerializer,
                                 NotaWriteSerializer)

    @action(detail=False, methods=["GET"], name="Get Filters", url_path="filters")
    def get_filters(self, request, *args, **kwargs):
        return Response(data={'filters': self.filterset_fields}, status=status.HTTP_200_OK)


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
