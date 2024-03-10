from fedhr.api.mixins import ApiAuthMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from fedhr.employee.models import EmploymentStatus, EmploymentStatusType


class EmploymentStatusViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class EmployeeSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            first_name = serializers.CharField(max_length=255, required=False)
            last_name = serializers.CharField(max_length=255, required=False)

        class EmploymentStatusTypeSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            employment_status_type_name = serializers.CharField(max_length=255, required=True)

        employee = EmployeeSerializer()
        employment_status_type = EmploymentStatusTypeSerializer()

        class Meta:
            model = EmploymentStatus
            fields = ['id', 'employee', 'effective_date', 'employment_status_type', 'comment']

    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = EmploymentStatus
            fields = ['id', 'employee', 'effective_date', 'employment_status_type', 'comment']

    queryset = EmploymentStatus.objects.all()
    serializer_class = OutputSerializer
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return self.OutputSerializer
        return self.InputSerializer


class EmploymentStatusTypeViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = EmploymentStatusType
            fields = ['id', 'employment_status_type_name']

    queryset = EmploymentStatusType.objects.all()
    serializer_class = OutputSerializer
    pagination_class = None
