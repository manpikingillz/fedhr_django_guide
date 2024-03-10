from fedhr.api.mixins import ApiAuthMixin
from fedhr.employee.models import Asset, AssetCategory
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers


class AssetViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class EmployeeSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            first_name = serializers.CharField(max_length=255, required=False)
            last_name = serializers.CharField(max_length=255, required=False)

        class AssetCategorySerializer(serializers.Serializer):
            id = serializers.IntegerField()
            asset_category_name = serializers.CharField(max_length=255)


        employee = EmployeeSerializer()
        asset_category = AssetCategorySerializer()

        class Meta:
            model = Asset
            fields = ['id', 'employee', 'asset_category', 'description', 'serial_number', 'date_assigned', 'date_returned']

    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Asset
            fields = ['id', 'employee', 'asset_category', 'description', 'serial_number', 'date_assigned', 'date_returned']

    queryset = Asset.objects.all()
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return self.OutputSerializer
        return self.InputSerializer


class AssetCategoryViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = AssetCategory
            fields = ['id', 'asset_category_name']

    queryset = AssetCategory.objects.all()
    serializer_class = OutputSerializer
    pagination_class = None
