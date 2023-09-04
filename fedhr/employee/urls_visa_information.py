from django.urls import path

from fedhr.employee.api.visa_information import (
    VisaInformationCreateApi,
    VisaInformationListApi,
    VisaInformationUpdateApi,
    VisaInformationDeleteApi,
)

urlpatterns = [
    path('create/', VisaInformationCreateApi.as_view(), name='visa_information_create'),
    path('', VisaInformationListApi.as_view(), name='visa_information_list'),
    path('<int:visa_information_id>/update/', VisaInformationUpdateApi.as_view(), name='visa_information_update'),
    path('<int:visa_information_id>/delete/', VisaInformationDeleteApi.as_view(), name='visa_information_delete'),
]