"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.escuela import views as escuela_views
from rest_framework.authtoken import views as authtoken_views

router = routers.DefaultRouter()
router.register(r'estudiante', escuela_views.EstudianteViewSet)
router.register(r'profesor', escuela_views.ProfesorViewSet)
router.register(r'profesorguia', escuela_views.ProfesorGuiaViewSet)
router.register(r'grupo', escuela_views.GrupoViewSet)
router.register(r'grado', escuela_views.GradoViewSet)
router.register(r'asignatura', escuela_views.AsignaturaViewSet)
router.register(r'nota', escuela_views.NotaViewSet)
router.register(r'curso', escuela_views.CursoViewSet)
router.register(r'programadeestudio', escuela_views.ProgramaDeEstudioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', authtoken_views.obtain_auth_token),
]
