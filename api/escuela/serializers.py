from rest_framework import serializers
from .models import Estudiante, Profesor, ProfesorGuia, ProgramaDeEstudio, Curso, Grado, Grupo, Nota, \
    Asignatura


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'


class ProfesorGuiaSerializer(serializers.ModelSerializer):
    profesor = ProfesorSerializer()

    class Meta:
        model = ProfesorGuia
        fields = ['grupo', 'profesor']


class GradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grado
        fields = '__all__'


class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'


class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class ProgramaDeEstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaDeEstudio
        fields = '__all__'


