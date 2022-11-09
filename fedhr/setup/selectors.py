from django.db.models.query import QuerySet
from fedhr.setup.models import Country


def country_list() -> QuerySet[Country]:
    return Country.objects.all()