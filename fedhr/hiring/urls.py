from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fedhr.hiring.api.template import TemplateViewSet

urlpatterns = []

router = DefaultRouter()
router.register(r'template', TemplateViewSet, basename='template')

urlpatterns = urlpatterns + [path('', include(router.urls)),]
