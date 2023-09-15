from fedhr.api.mixins import ApiAuthMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from fedhr.employee.models import JobInformation
from fedhr.employee.models import EmergencyContact
from fedhr.employee.models import Relationship


class EmergencyContactViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class EmployeeSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            first_name = serializers.CharField(max_length=255, required=False)
            last_name = serializers.CharField(max_length=255, required=False)

        class RelationshipSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            relationship_name = serializers.CharField(max_length=255)

        class CountrySerializer(serializers.Serializer):
            id = serializers.IntegerField()
            country_name = serializers.CharField(max_length=255)

        employee = EmployeeSerializer()
        relationship = RelationshipSerializer()
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


class RelationshipViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Relationship
            fields = ['id', 'relationship_name']

    queryset = Relationship.objects.all()
    serializer_class = OutputSerializer
    pagination_class = None
