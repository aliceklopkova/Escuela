from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers

from .models import Estudiante, Profesor, ProfesorGuia, ProgramaDeEstudio, Curso, Grado, Grupo, Nota, \
    Asignatura


class PermissionSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Permission
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()
    permissions = PermissionSerializer(many=True)

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Group
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()
    groups = GroupSerializer(many=True)

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = User
        fields = '__all__'


class GradoSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Grado
        fields = '__all__'


class GrupoReadSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()
    grado = GradoSerializer()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Grupo
        fields = '__all__'


class GrupoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'


class AsignaturaSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Asignatura
        fields = '__all__'


class EstudianteReadSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()
    grado = GradoSerializer()
    grupo = GrupoReadSerializer()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Estudiante
        fields = ['id', 'nombre', 'primer_apellido', 'segundo_apellido', 'fecha_nacimiento', 'ci', 'direccion',
                  'numero_telefono', 'reparto', 'municipio', 'provincia', 'genero', 'edad', 'nombre_apellido_padre',
                  'nombre_apellido_madre', 'grado', 'grupo', 'object_name']


class EstudianteWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


class ProfesorReadSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()
    grupos = GrupoReadSerializer(many=True)
    asignaturas = AsignaturaSerializer(many=True)

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Profesor
        fields = ['id', 'nombre', 'primer_apellido', 'segundo_apellido', 'fecha_nacimiento', 'ci', 'direccion',
                  'numero_telefono', 'reparto', 'municipio', 'provincia', 'genero', 'edad', 'grado_academico',
                  'categoria_docente', 'grupos', 'asignaturas', 'object_name']


class ProfesorWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'


class ProfesorReadGuiaSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()
    profesor = ProfesorReadSerializer()
    grupo = GrupoReadSerializer()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = ProfesorGuia
        fields = ['id', 'grupo', 'profesor', 'object_name']


class ProfesorWriteGuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfesorGuia
        fields = '__all__'


class NotaReadSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()
    estudiante = EstudianteReadSerializer()
    asignatura = AsignaturaSerializer()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Nota
        fields = '__all__'


class NotaWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Curso
        fields = '__all__'


class ProgramaDeEstudioReadSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()
    asignatura = AsignaturaSerializer()
    curso = CursoSerializer()
    grado = GradoSerializer()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = ProgramaDeEstudio
        fields = '__all__'


class ProgramaDeEstudioWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaDeEstudio
        fields = '__all__'


class NotaPromedioGradoSerializer(serializers.Serializer):
    grado = serializers.CharField()
