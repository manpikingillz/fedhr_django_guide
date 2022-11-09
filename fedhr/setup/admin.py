from django.contrib import admin
from fedhr.setup.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name',)
