from fedhr.setup.selectors import country_list
from rest_framework import serializers
from rest_framework.views import APIView
from fedhr.api.mixins import ApiAuthMixin
from rest_framework.response import Response

from fedhr.setup.models import Country
from rest_framework.viewsets import ModelViewSet


class CountryViewSet(ApiAuthMixin, ModelViewSet):
    '''
    I am choosing to use the ModelViewSet here because
    I want to use the default methods that are already
    implemented in the ModelViewSet class.

    Since I am using the ModelViewSet, I don't need to
    define the get method

    For Small models like Country and others, it will be
    hectict to create services (for create, update, delete)
    and selectors (for list, retrieve). Also defining
    plain Serializers for small models is hectic too,
    if they models are many.

    I will continue to use plain serializers, services,
    and selectors approach for other bigger models whose
    CRUD operations might be reused else where in the codebase. 
    I might actually use Model Serializers for those bigger models
    as well if the fields are to many, but then keep APIView approach
    where I define the get / post.
    '''
    # class OutputSerializer(serializers.Serializer):
    #     id = serializers.IntegerField()
    #     country_name = serializers.CharField(required=True)

    # Just using the ModelSerializer here so that I don't have to type out
    # the fields manully on the plain serializer.

    # Using get because we're using APIView.
    # def get(self, request):
    #     countries = country_list()

    #     data = self.OutputSerializer(countries, many=True).data
    #     return Response(data)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Country
            fields = ['id', 'country_name']

    # Applied on the ModelViewSet, and ultimately to the APIView through GenericAPIView
    queryset = Country.objects.all()
    serializer_class = OutputSerializer

    # In GenericAPIView, we have pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    # and we have DEFAULT_PAGINATION_CLASS set in our settings.py (base.py) file.
    # So if we don't include this line, we will get a paginated response.
    pagination_class = None


