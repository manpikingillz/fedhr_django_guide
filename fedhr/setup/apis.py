from fedhr.setup.selectors import country_list
from rest_framework import serializers
from rest_framework.views import APIView
from fedhr.api.mixins import ApiAuthMixin
from rest_framework.response import Response


class CountryListApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        country_name = serializers.CharField(required=True)

    def get(self, request):
        countries = country_list()

        data = self.OutputSerializer(countries, many=True).data
        return Response(data)