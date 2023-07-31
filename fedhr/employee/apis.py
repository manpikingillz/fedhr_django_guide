from fedhr.setup.models import Country
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from fedhr.api.mixins import ApiAuthMixin
from fedhr.common.utils import get_object
from fedhr.employee.services import employee_create, employee_update, employee_delete
from fedhr.employee.selectors import employee_detail, employee_list
from fedhr.employee.models import Employee
from drf_yasg.utils import swagger_auto_schema


class EmployeeCreateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        # Basic Information
        first_name = serializers.CharField(max_length=255, required=True)
        middle_name = serializers.CharField(max_length=255, required=False)
        last_name = serializers.CharField(max_length=255, required=True)
        preferred_name = serializers.CharField(max_length=255, required=False)
        gender = serializers.ChoiceField(
            choices=Employee.Gender.choices, required=False)
        date_of_birth = serializers.DateField(required=False)
        marital_status = serializers.ChoiceField(
            choices=Employee.MaritalStatus.choices, required=False)
        nationality = serializers.PrimaryKeyRelatedField(
            queryset=Country.objects.all(), required=False)

        # Job
        hire_date = serializers.DateField(required=False)

        # Identification Information
        social_security_number = serializers.CharField(max_length=50, required=False)
        national_identification_number = serializers.CharField(max_length=50, required=False)
        tax_identification_number = serializers.CharField(max_length=50, required=False)

        # Contact Information
        email = serializers.EmailField(max_length=255, required=False)
        home_email = serializers.EmailField(max_length=255, required=False)
        mobile_number = serializers.CharField(max_length=50, required=False)
        work_phone = serializers.CharField(max_length=50, required=False)
        home_phone = serializers.CharField(max_length=50, required=False)

        # Address Information.
        street1 = serializers.CharField(max_length=255, required=False)
        street2 = serializers.CharField(max_length=255, required=False)
        city = serializers.CharField(max_length=255, required=False)
        province = serializers.CharField(max_length=255, required=False)
        country = serializers.CharField(max_length=255, required=False)
        zip_code = serializers.CharField(max_length=255, required=False)

        # Social Information.
        linked_in = serializers.CharField(max_length=255, required=False)
        facebook = serializers.CharField(max_length=255, required=False)
        twitter = serializers.CharField(max_length=255, required=False)
        instagram = serializers.CharField(max_length=255, required=False)

    class OutputSerializer(serializers.Serializer):
        # Basic Information
        first_name = serializers.CharField(max_length=255, required=True)
        middle_name = serializers.CharField(max_length=255, required=False)
        last_name = serializers.CharField(max_length=255, required=True)
        preferred_name = serializers.CharField(max_length=255, required=False)
        gender = serializers.ChoiceField(
            choices=Employee.Gender.choices, required=False)
        date_of_birth = serializers.DateField(required=False)
        marital_status = serializers.ChoiceField(
            choices=Employee.MaritalStatus.choices, required=False)
        nationality = serializers.PrimaryKeyRelatedField(
            queryset=Country.objects.all(), required=False)

        # Job
        hire_date = serializers.DateField(required=False)

        # Identification Information
        social_security_number = serializers.CharField(max_length=50, required=False)
        national_identification_number = serializers.CharField(max_length=50, required=False)
        tax_identification_number = serializers.CharField(max_length=50, required=False)

        # Contact Information
        email = serializers.EmailField(max_length=255, required=False)
        home_email = serializers.EmailField(max_length=255, required=False)
        mobile_number = serializers.CharField(max_length=50, required=False)
        work_phone = serializers.CharField(max_length=50, required=False)
        home_phone = serializers.CharField(max_length=50, required=False)

        # Address Information.
        street1 = serializers.CharField(max_length=255, required=False)
        street2 = serializers.CharField(max_length=255, required=False)
        city = serializers.CharField(max_length=255, required=False)
        province = serializers.CharField(max_length=255, required=False)
        country = serializers.CharField(max_length=255, required=False)
        zip_code = serializers.CharField(max_length=255, required=False)

        # Social Information.
        linked_in = serializers.CharField(max_length=255, required=False)
        facebook = serializers.CharField(max_length=255, required=False)
        twitter = serializers.CharField(max_length=255, required=False)
        instagram = serializers.CharField(max_length=255, required=False)

    @swagger_auto_schema(
        description="Method to add a new Employee.",
        request_body=InputSerializer,
        responses={200: InputSerializer(many=False),
                   401: 'Unauthorized',
                   201: 'Employee Added'},
        tags=['Create / List Employees'],
        operation_description="Method to post a new Employee",
    )
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if employee := employee_create(**serializer.validated_data):
            employee = employee_detail(pk=employee.id)
            data = self.OutputSerializer(employee).data
        else:
            data = {}

        return Response(data=data, status=status.HTTP_201_CREATED)

# ApiAuthMixin, 
class EmployeeListApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        first_name = serializers.CharField(max_length=255, required=True)
        last_name = serializers.CharField(max_length=255, required=True)
        middle_name = serializers.CharField(max_length=255, required=False)
        full_name = serializers.CharField()
        gender = serializers.ChoiceField(choices=Employee.Gender.choices, required=True)
        email = serializers.EmailField(max_length=255, required=True)

    class FilterSerializer(serializers.Serializer):
        first_name = serializers.CharField(max_length=255, required=False)
        last_name = serializers.CharField(max_length=255, required=False)
        email = serializers.EmailField(max_length=255, required=False)

    @swagger_auto_schema(
        responses={200: OutputSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No Employees found'},
        tags=['Create / List Employees'],
        operation_description="Method to fetch all the Employees",
    )
    def get(self, request):
        # Make sure the filters are valid
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        employees = employee_list(filters=filters_serializer.validated_data)

        data = self.OutputSerializer(employees, many=True).data
        return Response(data)


class EmployeeDetailApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        # Basic Information
        first_name = serializers.CharField(max_length=255, required=True)
        middle_name = serializers.CharField(max_length=255, required=False)
        last_name = serializers.CharField(max_length=255, required=True)
        preferred_name = serializers.CharField(max_length=255, required=False)
        gender = serializers.ChoiceField(
            choices=Employee.Gender.choices, required=False)
        date_of_birth = serializers.DateField(required=False)
        marital_status = serializers.ChoiceField(
            choices=Employee.MaritalStatus.choices, required=False)
        nationality = serializers.PrimaryKeyRelatedField(
            queryset=Country.objects.all(), required=False)

        # Job
        hire_date = serializers.DateField(required=False)

        # Identification Information
        social_security_number = serializers.CharField(max_length=50, required=False)
        national_identification_number = serializers.CharField(max_length=50, required=False)
        tax_identification_number = serializers.CharField(max_length=50, required=False)

        # Contact Information
        email = serializers.EmailField(max_length=255, required=False)
        home_email = serializers.EmailField(max_length=255, required=False)
        mobile_number = serializers.CharField(max_length=50, required=False)
        work_phone = serializers.CharField(max_length=50, required=False)
        home_phone = serializers.CharField(max_length=50, required=False)

        # Address Information.
        street1 = serializers.CharField(max_length=255, required=False)
        street2 = serializers.CharField(max_length=255, required=False)
        city = serializers.CharField(max_length=255, required=False)
        province = serializers.CharField(max_length=255, required=False)
        country = serializers.CharField(max_length=255, required=False)
        zip_code = serializers.CharField(max_length=255, required=False)

        # Social Information.
        linked_in = serializers.CharField(max_length=255, required=False)
        facebook = serializers.CharField(max_length=255, required=False)
        twitter = serializers.CharField(max_length=255, required=False)
        instagram = serializers.CharField(max_length=255, required=False)

    def get(self, request, employee_id):

        employee = employee_detail(pk=employee_id)

        data = self.OutputSerializer(employee).data
        return Response(data)


class EmployeeUpdateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        # Basic Information
        first_name = serializers.CharField(max_length=255, required=False)
        middle_name = serializers.CharField(max_length=255, required=False)
        last_name = serializers.CharField(max_length=255, required=False)
        preferred_name = serializers.CharField(max_length=255, required=False)
        gender = serializers.ChoiceField(
            choices=Employee.Gender.choices, required=False)
        date_of_birth = serializers.DateField(required=False)
        marital_status = serializers.ChoiceField(
            choices=Employee.MaritalStatus.choices, required=False)
        nationality = serializers.PrimaryKeyRelatedField(
            queryset=Country.objects.all(), required=False)

        # Job
        hire_date = serializers.DateField(required=False)

        # Identification Information
        social_security_number = serializers.CharField(max_length=50, required=False)
        national_identification_number = serializers.CharField(max_length=50, required=False)
        tax_identification_number = serializers.CharField(max_length=50, required=False)

        # Contact Information
        email = serializers.EmailField(max_length=255, required=False)
        home_email = serializers.EmailField(max_length=255, required=False)
        mobile_number = serializers.CharField(max_length=50, required=False)
        work_phone = serializers.CharField(max_length=50, required=False)
        home_phone = serializers.CharField(max_length=50, required=False)

        # Address Information.
        street1 = serializers.CharField(max_length=255, required=False)
        street2 = serializers.CharField(max_length=255, required=False)
        city = serializers.CharField(max_length=255, required=False)
        province = serializers.CharField(max_length=255, required=False)
        country = serializers.CharField(max_length=255, required=False)
        zip_code = serializers.CharField(max_length=255, required=False)

        # Social Information.
        linked_in = serializers.CharField(max_length=255, required=False)
        facebook = serializers.CharField(max_length=255, required=False)
        twitter = serializers.CharField(max_length=255, required=False)
        instagram = serializers.CharField(max_length=255, required=False)

    def post(self, request, employee_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employee = get_object(Employee, pk=employee_id)

        employee_update(employee=employee, data=serializer.validated_data)
        return Response(status=status.HTTP_200_OK)


class EmployeeDeleteApi(ApiAuthMixin, APIView):
    def post(self, request, employee_id):
        employee = get_object(Employee, pk=employee_id)

        employee_delete(employee=employee)

        return Response(status=status.HTTP_200_OK)
