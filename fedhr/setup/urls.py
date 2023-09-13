from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .apis import (
    CountryViewSet
)

router = DefaultRouter()
router.register(r'country', CountryViewSet, basename='country')

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('country-list/', CountryApi.as_view(), name='country_list')
# ]
