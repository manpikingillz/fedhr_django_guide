from fedhr.api.mixins import ApiAuthMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from fedhr.employee.models import JobInformation
from fedhr.employee.models import EmergencyContact


class EmergencyContactViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class EmployeeSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            first_name = serializers.CharField(max_length=255, required=False)
            last_name = serializers.CharField(max_length=255, required=False)

        class CountrySerializer(serializers.Serializer):
            id = serializers.IntegerField()
            country_name = serializers.CharField(max_length=255)

        employee = EmployeeSerializer()
        nationality = CountrySerializer()

        class Meta:
            model = EmergencyContact
            fields = ['id', 'employee', 'name', 'relationship', 'mobile_phone', 'home_phone', 'work_phone', 'home_email', 'work_email', 'address', 'city', 'province', 'nationality', 'is_primary_contact']

    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = EmergencyContact
            fields = ['id', 'employee', 'name', 'relationship', 'mobile_phone', 'home_phone', 'work_phone', 'home_email', 'work_email', 'address', 'city', 'province', 'nationality', 'is_primary_contact']

    queryset = EmergencyContact.objects.all()
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return self.OutputSerializer
        return self.InputSerializer
