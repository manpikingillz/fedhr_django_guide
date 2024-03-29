from django.urls import path

from fedhr.employee.api.employee import (
    EmployeeCreateApi,
    EmployeeListApi,
    EmployeeDetailApi,
    EmployeeUpdateApi,
    EmployeeDeleteApi,
)


urlpatterns = [
    path('create/', EmployeeCreateApi.as_view(), name='employee_create'),
    path('', EmployeeListApi.as_view(), name='employee_list'),
    path('<int:employee_id>/', EmployeeDetailApi.as_view(), name='employee_detail'),
    path('<int:employee_id>/update/', EmployeeUpdateApi.as_view(), name='employee_update'),
    path('<int:employee_id>/delete/', EmployeeDeleteApi.as_view(), name='employee_delete')
]




