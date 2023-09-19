from fedhr.api.mixins import ApiAuthMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from fedhr.hiring.models import Template


class TemplateViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Template
            fields = ['id', 'template_name', 'template']

    queryset = Template.objects.all()
    serializer_class = OutputSerializer
    pagination_class = None
