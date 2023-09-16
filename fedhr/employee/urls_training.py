from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fedhr.employee.api.training import (
    TrainingViewSet,
    CourseViewSet
)

urlpatterns = []

router = DefaultRouter()
router.register(r'training', TrainingViewSet, basename='training')
router.register(r'course', CourseViewSet, basename='course')


urlpatterns = urlpatterns + [path('', include(router.urls)),]