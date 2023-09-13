from fedhr.api.mixins import ApiAuthMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from fedhr.employee.models import EmploymentStatus


class EmploymentStatusViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class EmploymentStatusTypeSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            employment_status_type_name = serializers.CharField(max_length=255, required=True)

        employment_status_type = EmploymentStatusTypeSerializer()

        class Meta:
            model = EmploymentStatus
            fields = ['id', 'employee', 'effective_date', 'employment_status_type', 'comment']
    queryset = EmploymentStatus.objects.all()
    serializer_class = OutputSerializer
    pagination_class = None
