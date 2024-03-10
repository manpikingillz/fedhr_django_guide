from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fedhr.employee.api.job_information import (
    JobInformationViewSet,
    LocationViewSet,
    DivisionViewSet,
    DepartmentViewSet,
    JobViewSet
)

urlpatterns = []

router = DefaultRouter()
router.register(r'job-information', JobInformationViewSet, basename='job_information')
router.register(r'location', LocationViewSet, basename='location')
router.register(r'division', DivisionViewSet, basename='division')
router.register(r'department', DepartmentViewSet, basename='department')
router.register(r'job', JobViewSet, basename='job')

urlpatterns = urlpatterns + [path('', include(router.urls)),]