from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fedhr.hiring.api.job_opening import (
    JobOpeningViewSet,
    EmploymentTypeViewSet
)

urlpatterns = []

router = DefaultRouter()
router.register(r'job-opening', JobOpeningViewSet, basename='job_opening')
router.register(r'employment-type', EmploymentTypeViewSet, basename='employment_type')


urlpatterns = urlpatterns + [path('', include(router.urls)),]