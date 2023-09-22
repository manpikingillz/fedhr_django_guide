from fedhr.hiring.models import JobOpening
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from fedhr.api.mixins import ApiAuthMixin


class JobOpeningViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class EmployeeSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            first_name = serializers.CharField(max_length=255, required=False)
            last_name = serializers.CharField(max_length=255, required=False)

        class DepartmentSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            department_name = serializers.CharField(max_length=255)

        class EmploymentTypeSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            employment_type_name = serializers.CharField(max_length=255)

        class LocationSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            location_name = serializers.CharField(max_length=255)

        class CountrySerializer(serializers.Serializer):
            id = serializers.IntegerField()
            country_name = serializers.CharField(max_length=255)


        hiring_lead = EmployeeSerializer()
        hiring_department = DepartmentSerializer()
        employment_type = EmploymentTypeSerializer()
        location = LocationSerializer()
        country = CountrySerializer()

        class Meta:
            model = JobOpening
            fields = ['id', 'job_title', 'job_status', 'hiring_lead',
                      'hiring_department', 'employment_type', 'minimum_experience',
                      'job_description', 'location', 'country', 'city', 'province', 'postal_code',
                      'compensation', 'created_at']

    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = JobOpening
            fields = ['id', 'job_title', 'job_status', 'hiring_lead',
                      'hiring_department', 'employment_type', 'minimum_experience',
                      'job_description', 'location', 'country', 'city', 'province', 'postal_code',
                      'compensation']

    class FilterSerializer(serializers.Serializer):
        reports_to_id = serializers.IntegerField()

    queryset = JobOpening.objects.all()
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return self.OutputSerializer
        return self.InputSerializer

    # @action(detail=False, methods=['GET'], name='Get Direct Reports')
    # def get_direct_reports(self, request, *args, **kwargs):
    #     filters_serializer = self.FilterSerializer(data=request.query_params)
    #     filters_serializer.is_valid(raise_exception=True)

    #     direct_reports = direct_reports_list(filters=filters_serializer.validated_data)

    #     serializer = self.OutputSerializer.EmployeeSerializer(direct_reports, many=True)
    #     return Response(serializer.data)