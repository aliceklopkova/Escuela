from django.test import TestCase
from django.utils.timezone import now

from api.escuela.models import Estudiante


class EstudianteTestCase(TestCase):
    def setUp(self):
        self.estudiante = Estudiante.objects.create(
            nombre="Estudiante",
            primer_apellido="Test",
            segundo_apellido="Test2do",
            fecha_nacimiento=now().date(),
            ci="999999999",
            direccion="test_direction",
            numero_telefono="+5355555555",
            municipio="test_municipio",
            provincia="test_provincia",
            reparto="test_reparto",
            genero="M",
            nombre_apellido_madre="test_madre",
            nombre_apellido_padre="test_padre",
        )

    def test_get_estudiante(self):
        assert Estudiante.objects.get(primer_apellido="Test")

    def test_update_estudiante(self):
        new_estudiante = Estudiante.objects.get(primer_apellido="Test")
        new_estudiante.primer_apellido = "Update_Test"
        new_estudiante.save()
        assert Estudiante.objects.get(primer_apellido="Update_Test")

    def test_delete_estudiante(self):
        assert Estudiante.objects.get(primer_apellido="Test")
        Estudiante.objects.get(primer_apellido="Test").delete()
        self.assertFalse(Estudiante.objects.filter(primer_apellido="Test"))

    def test_create_estudiante(self):
        self.estudiante = Estudiante.objects.create(
            nombre="Estudiante2",
            primer_apellido="Test2",
            segundo_apellido="Test2do2",
            fecha_nacimiento=now().date(),
            ci="999999998",
            direccion="test_direction2",
            numero_telefono="+5355555554",
            municipio="test_municipio2",
            provincia="test_provincia2",
            reparto="test_reparto2",
            genero="M",
            nombre_apellido_madre="test_madre2",
            nombre_apellido_padre="test_padre2",
        )
        assert Estudiante.objects.get(primer_apellido="Test2")
