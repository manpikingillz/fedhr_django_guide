from fedhr.api.mixins import ApiAuthMixin
from fedhr.employee.models import Course, Training
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers


class TrainingViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class EmployeeSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            first_name = serializers.CharField(max_length=255, required=False)
            last_name = serializers.CharField(max_length=255, required=False)

        class CourseSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            course_name = serializers.CharField(max_length=255)


        employee = EmployeeSerializer()
        course = CourseSerializer()

        class Meta:
            model = Training
            fields = ['id', 'employee', 'course', 'completed', 'cost', 'credits', 'hours', 'instructor', 'note', 'attachments']

    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Training
            fields = ['id', 'employee', 'course', 'completed', 'cost', 'credits', 'hours', 'instructor', 'note', 'attachments']

    queryset = Training.objects.all()
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return self.OutputSerializer
        return self.InputSerializer


class CourseViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Course
            fields = ['id', 'course_name']

    queryset = Course.objects.all()
    serializer_class = OutputSerializer
    pagination_class = None
