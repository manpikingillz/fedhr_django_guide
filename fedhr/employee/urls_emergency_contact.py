from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fedhr.employee.api.emergency_contact import (
    EmergencyContactViewSet,
    RelationshipViewSet
)

urlpatterns = []

router = DefaultRouter()
router.register(r'emergency-contact', EmergencyContactViewSet, basename='emergency_contact')
router.register(r'relationship', RelationshipViewSet, basename='relationship')


urlpatterns = urlpatterns + [path('', include(router.urls)),]