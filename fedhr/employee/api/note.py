from fedhr.employee.models import Note
from fedhr.employee.selectors import note_detail, note_list
from fedhr.employee.services import note_create, note_delete, note_update
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from fedhr.api.mixins import ApiAuthMixin
from fedhr.common.utils import get_object
from fedhr.employee.models import Employee
from drf_yasg.utils import swagger_auto_schema

from fedhr.api.pagination import LimitOffsetPagination


class NoteCreateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        note = serializers.CharField(required=True)
        employee = serializers.PrimaryKeyRelatedField(
            queryset=Employee.objects.all(), required=True)

    class OutputSerializer(serializers.Serializer):
        note = serializers.CharField(required=True)
        employee = serializers.PrimaryKeyRelatedField(
            queryset=Employee.objects.all(), required=True)

    # @swagger_auto_schema(
    #     description="Method to add a new Note.",
    #     request_body=InputSerializer,
    #     responses={200: InputSerializer(many=False),
    #                401: 'Unauthorized',
    #                201: 'Note Added'},
    #     tags=['Create / List Notes'],
    #     operation_description="Method to post a new Note",
    # )
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if note := note_create(**serializer.validated_data):
            note = note_detail(pk=note.id)
            data = self.OutputSerializer(note).data
        else:
            data = {}

        return Response(data=data, status=status.HTTP_201_CREATED)


class NoteListApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        class EmployeeSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            first_name = serializers.CharField(max_length=255, required=False)
            last_name = serializers.CharField(max_length=255, required=False)

        id = serializers.IntegerField()
        note = serializers.CharField(max_length=255, required=True)
        employee = EmployeeSerializer()
        # employee = serializers.PrimaryKeyRelatedField(
        #     queryset=Employee.objects.all(), required=True)
        created_at = serializers.DateTimeField()

    class FilterSerializer(serializers.Serializer):
        note = serializers.CharField(max_length=255, required=False)
        employee = serializers.PrimaryKeyRelatedField(
            queryset=Employee.objects.all(), required=False)

    # @swagger_auto_schema(
    #     responses={200: OutputSerializer(many=True),
    #                401: 'Unauthorized',
    #                404: 'No Notes found'},
    #     tags=['Create / List Notes'],
    #     operation_description="Method to fetch all the Notes",
    # )
    def get(self, request):
        # Make sure the filters are valid
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        notes = note_list(filters=filters_serializer.validated_data)

        paginator = LimitOffsetPagination()

        # Get paginated result
        result_page = paginator.paginate_queryset(notes, request)
        if result_page is not None:
            data = self.OutputSerializer(result_page, many=True).data
            return paginator.get_paginated_response(data)

        data = self.OutputSerializer(notes, many=True).data
        return Response(data)


class NoteDetailApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        note = serializers.CharField(max_length=255, required=True)
        employee = serializers.PrimaryKeyRelatedField(
            queryset=Employee.objects.all(), required=True)

    def get(self, request, note_id):
        note = note_detail(pk=note_id)

        data = self.OutputSerializer(note).data
        return Response(data)


class NoteUpdateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        note = serializers.CharField(max_length=255, required=True)
        employee = serializers.PrimaryKeyRelatedField(
            queryset=Employee.objects.all(), required=True)

    def post(self, request, note_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        note = get_object(Note, pk=note_id)

        note_update(note=note, data=serializer.validated_data)
        return Response(status=status.HTTP_200_OK)


class NoteDeleteApi(ApiAuthMixin, APIView):
    def post(self, request, note_id):
        note = get_object(Note, pk=note_id)

        note_delete(note=note)

        return Response(status=status.HTTP_200_OK)
