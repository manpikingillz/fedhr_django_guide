from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fedhr.employee.api.education import (
    EducationCreateApi,
    EducationListApi,
    EducationUpdateApi,
    EducationDeleteApi,

    EducationAwardViewSet
)



urlpatterns = [
    path('create/', EducationCreateApi.as_view(), name='education_create'),
    path('', EducationListApi.as_view(), name='education_list'),
    path('<int:education_id>/update/', EducationUpdateApi.as_view(), name='education_update'),
    path('<int:education_id>/delete/', EducationDeleteApi.as_view(), name='education_delete'),
]

router = DefaultRouter()
router.register(r'education_awards', EducationAwardViewSet, basename='education_awards')

urlpatterns = urlpatterns + [path('', include(router.urls)),]