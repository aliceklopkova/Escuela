from rest_framework import serializers

from .models import Estudiante, Profesor, ProfesorGuia, ProgramaDeEstudio, Curso, Grado, Grupo, Nota, \
    Asignatura


class EstudianteSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Estudiante
        fields = ['id', 'nombre', 'primer_apellido', 'segundo_apellido', 'fecha_nacimiento', 'ci', 'direccion',
                  'numero_telefono', 'reparto', 'municipio', 'provincia', 'genero', 'edad', 'nombre_apellido_padre',
                  'nombre_apellido_madre', 'grado', 'grupo', 'object_name']


class ProfesorSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Profesor
        fields = ['id', 'nombre', 'primer_apellido', 'segundo_apellido', 'fecha_nacimiento', 'ci', 'direccion',
                  'numero_telefono', 'reparto', 'municipio', 'provincia', 'genero', 'edad', 'grado_academico',
                  'categoria_docente', 'grupos', 'asignaturas', 'object_name']


class ProfesorGuiaSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = ProfesorGuia
        fields = ['id', 'grupo', 'profesor', 'object_name']


class GradoSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Grado
        fields = '__all__'


class AsignaturaSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Asignatura
        fields = '__all__'


class GrupoSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Grupo
        fields = '__all__'


class NotaSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()

    def get_object_name(self, obj):
        return obj.__str__()

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


class ProgramaDeEstudioSerializer(serializers.ModelSerializer):
    object_name = serializers.SerializerMethodField()

    def get_object_name(self, obj):
        return obj.__str__()

    class Meta:
        model = ProgramaDeEstudio
        fields = '__all__'
