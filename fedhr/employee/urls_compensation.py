from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fedhr.employee.api.compensation import (
    CompensationViewSet,
    CurrencyViewSet,
    ChangeReasonViewSet
)

urlpatterns = []

router = DefaultRouter()
router.register(r'compensation', CompensationViewSet, basename='compensation')
router.register(r'currency', CurrencyViewSet, basename='currency')
router.register(r'change-reason', ChangeReasonViewSet, basename='change-reason')

urlpatterns = urlpatterns + [path('', include(router.urls)),]