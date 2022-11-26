from django.test import TestCase
from django.utils.timezone import now

from api.escuela.models import Estudiante


class EstudianteTestCase(TestCase):

    def test_estudiante_crud(self):
        # Create Estudiante
        Estudiante.objects.create(
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
        # Get Estudiante
        assert Estudiante.objects.get(primer_apellido="Test")
        # Update Estudiante
        self.estudiante = Estudiante.objects.get(primer_apellido="Test")
        self.estudiante.primer_apellido = "Update_Test"
        self.estudiante.save()
        assert Estudiante.objects.get(primer_apellido="Update_Test")
        # Delete Estudiante
        Estudiante.objects.get(primer_apellido="Update_Test").delete()
        self.assertFalse(Estudiante.objects.filter(primer_apellido="Update_Test"))
