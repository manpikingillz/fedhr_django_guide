from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fedhr.employee.api.employment_status import (
    EmploymentStatusViewSet
)

urlpatterns = []

router = DefaultRouter()
router.register(r'employment-status', EmploymentStatusViewSet, basename='employment_status')

urlpatterns = urlpatterns + [path('', include(router.urls)),]