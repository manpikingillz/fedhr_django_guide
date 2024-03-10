from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fedhr.employee.api.employment_status import (
    EmploymentStatusViewSet,
    EmploymentStatusTypeViewSet
)

urlpatterns = []

router = DefaultRouter()
router.register(r'employment-status', EmploymentStatusViewSet, basename='employment_status')
router.register(r'employment-status-type', EmploymentStatusTypeViewSet, basename='employment_status_type')


urlpatterns = urlpatterns + [path('', include(router.urls)),]