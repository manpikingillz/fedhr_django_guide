from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fedhr.hiring.api.job_opening import (
    JobOpeningViewSet,
)

urlpatterns = []

router = DefaultRouter()
router.register(r'job-opening', JobOpeningViewSet, basename='job_opening')


urlpatterns = urlpatterns + [path('', include(router.urls)),]