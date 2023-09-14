from fedhr.api.mixins import ApiAuthMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from fedhr.employee.models import Compensation
from fedhr.employee.models import ChangeReason, Currency


class CompensationViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class EmployeeSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            first_name = serializers.CharField(max_length=255, required=False)
            last_name = serializers.CharField(max_length=255, required=False)

        class CurrencySerializer(serializers.Serializer):
            id = serializers.IntegerField()
            currency_name = serializers.CharField(max_length=255)
            currency_code = serializers.CharField(max_length=3)

        class ChangeReasonSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            change_reason_name = serializers.CharField(max_length=255)

        employee = EmployeeSerializer()
        pay_rate_currency = CurrencySerializer()
        change_reason = ChangeReasonSerializer()


        class Meta:
            model = Compensation
            fields = ['id', 'employee', 'effective_date', 'pay_type', 'pay_rate', 'pay_rate_currency', 'pay_rate_period', 'pay_schedule', 'overtime_status', 'change_reason', 'payment_method', 'comment']

    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Compensation
            fields = ['id', 'employee', 'effective_date', 'pay_type', 'pay_rate', 'pay_rate_currency', 'pay_rate_period', 'pay_schedule', 'overtime_status', 'change_reason', 'payment_method', 'comment']

    queryset = Compensation.objects.all()
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return self.OutputSerializer
        return self.InputSerializer


class CurrencyViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Currency
            fields = ['id', 'currency_name', 'currency_code']

    queryset = Currency.objects.all()
    serializer_class = OutputSerializer
    pagination_class = None


class ChangeReasonViewSet(ApiAuthMixin, ModelViewSet):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = ChangeReason
            fields = ['id', 'change_reason_name']

    queryset = ChangeReason.objects.all()
    serializer_class = OutputSerializer
    pagination_class = None
