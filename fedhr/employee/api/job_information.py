from fedhr.api.mixins import ApiAuthMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from fedhr.employee.models import JobInformation


class JobInformationViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class EmployeeSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            first_name = serializers.CharField(max_length=255, required=False)
            last_name = serializers.CharField(max_length=255, required=False)

        class LocationSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            location_name = serializers.CharField(max_length=255)

        class DivisionSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            division_name = serializers.CharField(max_length=255)

        class DepartmentSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            department_name = serializers.CharField(max_length=255)

        class JobSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            job_title_name = serializers.CharField(max_length=255)

        employee = EmployeeSerializer()
        location = LocationSerializer()
        division = DivisionSerializer()
        department = DepartmentSerializer()
        job = JobSerializer()
        reports_to = EmployeeSerializer()

        class Meta:
            model = JobInformation
            fields = ['id', 'employee', 'effective_date', 'location', 'division', 'department', 'job', 'reports_to']

    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = JobInformation
            fields = ['id', 'employee', 'effective_date', 'location', 'division', 'department', 'job', 'reports_to']

    queryset = JobInformation.objects.all()
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return self.OutputSerializer
        return self.InputSerializer


# class EmploymentStatusTypeViewSet(ApiAuthMixin, ModelViewSet):
#     class OutputSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = EmploymentStatusType
#             fields = ['id', 'employment_status_type_name']

#     queryset = EmploymentStatusType.objects.all()
#     serializer_class = OutputSerializer
#     pagination_class = None
