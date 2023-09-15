from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fedhr.employee.api.emergency_contact import (
    EmergencyContactViewSet,
)

urlpatterns = []

router = DefaultRouter()
router.register(r'emergency-contact', EmergencyContactViewSet, basename='emergency_contact')

urlpatterns = urlpatterns + [path('', include(router.urls)),]