from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fedhr.employee.api.asset import (
    AssetViewSet,
    AssetCategoryViewSet
)

urlpatterns = []

router = DefaultRouter()
router.register(r'asset', AssetViewSet, basename='asset')
router.register(r'asset-category', AssetCategoryViewSet, basename='asset_category')


urlpatterns = urlpatterns + [path('', include(router.urls)),]