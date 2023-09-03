from django.urls import path

from fedhr.employee.api.education import (
    EducationCreateApi,
    EducationListApi,
    EducationUpdateApi,
    EducationDeleteApi,
)

urlpatterns = [
    path('create/', EducationCreateApi.as_view(), name='education_create'),
    path('', EducationListApi.as_view(), name='education_list'),
    path('<int:education_id>/update/', EducationUpdateApi.as_view(), name='education_update'),
    path('<int:education_id>/delete/', EducationDeleteApi.as_view(), name='education_delete'),
]