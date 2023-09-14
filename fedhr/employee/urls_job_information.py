from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fedhr.employee.api.job_information import (
    JobInformationViewSet
)

urlpatterns = []

router = DefaultRouter()
router.register(r'job-information', JobInformationViewSet, basename='job_information')

urlpatterns = urlpatterns + [path('', include(router.urls)),]