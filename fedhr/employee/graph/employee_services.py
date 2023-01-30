from django.db import transaction
from django.core.exceptions import ValidationError

from fedhr.common.services import model_update
from fedhr.common.types import DjangoModelType
from fedhr.employee.models import Employee


def employee_create(
    *,
    first_name,
    last_name,
    # middle_name,
    country
) -> Employee:
    employee = Employee(
        first_name=first_name,
        last_name=last_name,
        # middle_name=middle_name,
        country=country
    )

    employee.full_clean()
    employee.save()

    return employee
