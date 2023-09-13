# Create an api for creating education records for an employee.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from fedhr.api.mixins import ApiAuthMixin
from fedhr.common.utils import get_object
from fedhr.employee.models import (
    Employee, Visa, Country, VisaInformation)
from drf_yasg.utils import swagger_auto_schema
from fedhr.employee.selectors import (
    visa_information_list, visa_information_detail)
from fedhr.employee.services import (
    visa_information_create, visa_information_update, visa_information_delete)
from fedhr.api.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet


class VisaInformationCreateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        employee = serializers.PrimaryKeyRelatedField(
            queryset=Employee.objects.all(), required=True)
        date = serializers.DateTimeField(required=False)
        visa = serializers.PrimaryKeyRelatedField(
            queryset=Visa.objects.all(), required=True)
        issued_date = serializers.DateTimeField(required=False)
        issuing_country = serializers.PrimaryKeyRelatedField(
            queryset=Country.objects.all(), required=True)
        expiration_date = serializers.DateTimeField(required=False)
        note = serializers.CharField(required=False)

    class OutputSerializer(serializers.Serializer):
        class EmployeeSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            first_name = serializers.CharField(max_length=255, required=False)
            last_name = serializers.CharField(max_length=255, required=False)

        class VisaSerializer(serializers.Serializer):
            visa_name = serializers.CharField(max_length=255, required=True)

        class CountrySerializer(serializers.Serializer):
            country_name = serializers.CharField(max_length=255, required=True)

        id = serializers.IntegerField()
        employee = EmployeeSerializer()
        date = serializers.DateTimeField(required=False)
        visa = VisaSerializer()
        issued_date = serializers.DateTimeField(required=False)
        issuing_country = CountrySerializer()
        expiration_date = serializers.DateTimeField(required=False)
        note = serializers.CharField(required=False)

    # @swagger_auto_schema(
    #     description="Method to add a new Visa Information.",
    #     request_body=InputSerializer,
    #     responses={200: InputSerializer(many=False),
    #                401: 'Unauthorized',
    #                201: 'Note Added'},
    #     tags=['Create / List Visa Informations'],
    #     operation_description="Method to post a new Visa Information",
    # )
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if visa_information := visa_information_create(**serializer.validated_data):
            visa_information = visa_information_detail(pk=visa_information.id)
            data = self.OutputSerializer(visa_information).data
        else:
            data = {}

        return Response(data=data, status=status.HTTP_201_CREATED)


class VisaInformationListApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        class EmployeeSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            first_name = serializers.CharField(max_length=255, required=False)
            last_name = serializers.CharField(max_length=255, required=False)

        class VisaSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            visa_name = serializers.CharField(max_length=255, required=True)

        class CountrySerializer(serializers.Serializer):
            id = serializers.IntegerField()
            country_name = serializers.CharField(max_length=255, required=True)

        id = serializers.IntegerField()
        employee = EmployeeSerializer()
        date = serializers.DateTimeField(required=False)
        visa = VisaSerializer()
        issued_date = serializers.DateTimeField(required=False)
        issuing_country = CountrySerializer()
        expiration_date = serializers.DateTimeField(required=False)
        note = serializers.CharField(required=False)

    class FilterSerializer(serializers.Serializer):
        employee = serializers.PrimaryKeyRelatedField(
            queryset=Employee.objects.all(), required=False)

    # @swagger_auto_schema(
    #     responses={200: OutputSerializer(many=True),
    #                401: 'Unauthorized',
    #                404: 'No Notes found'},
    #     tags=['Create / List Visa Informations'],
    #     operation_description="Method to fetch all the Visa Informations",
    # )
    def get(self, request):
        # Make sure the filters are valid
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        visa_informations = visa_information_list(filters=filters_serializer.validated_data)

        # paginator = LimitOffsetPagination()

        # # Get paginated result
        # result_page = paginator.paginate_queryset(visa_informations, request)
        # if result_page is not None:
        #     data = self.OutputSerializer(result_page, many=True).data
        #     return paginator.get_paginated_response(data)

        data = self.OutputSerializer(visa_informations, many=True).data
        return Response(data)


class VisaInformationUpdateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        employee = serializers.PrimaryKeyRelatedField(
            queryset=Employee.objects.all(), required=True)
        date = serializers.DateTimeField(required=False)
        visa = serializers.PrimaryKeyRelatedField(
            queryset=Visa.objects.all(), required=True)
        issued_date = serializers.DateTimeField(required=False)
        issuing_country = serializers.PrimaryKeyRelatedField(
            queryset=Country.objects.all(), required=True)
        expiration_date = serializers.DateTimeField(required=False)
        note = serializers.CharField(required=False)

    def post(self, request, note_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        visa_information = get_object(VisaInformation, pk=note_id)

        visa_information_update(visa_information=visa_information, data=serializer.validated_data)
        return Response(status=status.HTTP_200_OK)


class VisaInformationDeleteApi(ApiAuthMixin, APIView):
    def post(self, request, note_id):
        visa_information = get_object(VisaInformation, pk=note_id)

        visa_information_delete(visa_information=visa_information)

        return Response(status=status.HTTP_200_OK)


class VisaViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Visa
            fields = ['id', 'visa_name']

    queryset = Visa.objects.all()
    serializer_class = OutputSerializer
    pagination_class = None
