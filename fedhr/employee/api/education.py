# Create an api for creating education records for an employee.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from fedhr.api.mixins import ApiAuthMixin
from fedhr.common.utils import get_object
from fedhr.employee.models import Employee, Education, EducationAward
from drf_yasg.utils import swagger_auto_schema
from fedhr.employee.selectors import education_detail, education_list
from fedhr.employee.services import (
    education_create, education_delete, education_update)
from fedhr.api.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet


class EducationCreateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        employee = serializers.PrimaryKeyRelatedField(
            queryset=Employee.objects.all(), required=True)
        institution_name = serializers.CharField(required=True)
        award = serializers.PrimaryKeyRelatedField(
            queryset=EducationAward.objects.all(), required=True)
        major = serializers.CharField(required=False)
        start_date = serializers.DateField(required=False)
        end_date = serializers.DateField(required=False)
        score = serializers.CharField(required=False)

    class OutputSerializer(serializers.Serializer):
        employee = serializers.PrimaryKeyRelatedField(
            queryset=Employee.objects.all(), required=True)
        institution_name = serializers.CharField(required=True)
        award = serializers.PrimaryKeyRelatedField(
            queryset=EducationAward.objects.all(), required=True)
        major = serializers.CharField(required=False)
        start_date = serializers.DateField(required=False)
        end_date = serializers.DateField(required=False)
        score = serializers.CharField(required=False)

    # @swagger_auto_schema(
    #     description="Method to add a new Education.",
    #     request_body=InputSerializer,
    #     responses={200: InputSerializer(many=False),
    #                401: 'Unauthorized',
    #                201: 'Note Added'},
    #     tags=['Create / List Notes'],
    #     operation_description="Method to post a new Education",
    # )
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if education := education_create(**serializer.validated_data):
            education = education_detail(pk=education.id)
            data = self.OutputSerializer(education).data
        else:
            data = {}

        return Response(data=data, status=status.HTTP_201_CREATED)


class EducationListApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        class EmployeeSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            first_name = serializers.CharField(max_length=255, required=False)
            last_name = serializers.CharField(max_length=255, required=False)

        class EducationAwardSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            education_award_name = serializers.CharField(max_length=255, required=True)

        id = serializers.IntegerField()
        employee = EmployeeSerializer()
        institution_name = serializers.CharField(required=True)
        award = EducationAwardSerializer()
        major = serializers.CharField(required=False)
        start_date = serializers.DateField(required=False)
        end_date = serializers.DateField(required=False)
        score = serializers.CharField(required=False)

    class FilterSerializer(serializers.Serializer):
        institution_name = serializers.CharField(max_length=255, required=False)
        employee = serializers.PrimaryKeyRelatedField(
            queryset=Employee.objects.all(), required=False)

    # @swagger_auto_schema(
    #     responses={200: OutputSerializer(many=True),
    #                401: 'Unauthorized',
    #                404: 'No Notes found'},
    #     tags=['Create / List Education'],
    #     operation_description="Method to fetch all the Education",
    # )
    def get(self, request):
        # Make sure the filters are valid
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        educations = education_list(filters=filters_serializer.validated_data)

        # paginator = LimitOffsetPagination()

        # # Get paginated result
        # result_page = paginator.paginate_queryset(educations, request)
        # if result_page is not None:
        #     data = self.OutputSerializer(result_page, many=True).data
        #     return paginator.get_paginated_response(data)

        data = self.OutputSerializer(educations, many=True).data
        return Response(data)


class EducationUpdateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        employee = serializers.PrimaryKeyRelatedField(
            queryset=Employee.objects.all(), required=True)
        institution_name = serializers.CharField(required=True)
        award = serializers.PrimaryKeyRelatedField(
            queryset=EducationAward.objects.all(), required=True)
        major = serializers.CharField(required=False)
        start_date = serializers.DateField(required=False)
        end_date = serializers.DateField(required=False)
        score = serializers.CharField(required=False)

    def post(self, request, education_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        education = get_object(Education, pk=education_id)

        education_update(education=education, data=serializer.validated_data)
        return Response(status=status.HTTP_200_OK)


class EducationDeleteApi(ApiAuthMixin, APIView):
    def post(self, request, education_id):
        education = get_object(Education, pk=education_id)

        education_delete(education=education)

        return Response(status=status.HTTP_200_OK)


class EducationAwardViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = EducationAward
            fields = ['id', 'education_award_name']

    queryset = EducationAward.objects.all()
    serializer_class = OutputSerializer
    pagination_class = None
