from typing import List, Dict, Any, Tuple

from django.core.exceptions import ValidationError
from django.db import transaction

from fedhr.common.types import DjangoModelType


def model_update(
    *,
    instance: DjangoModelType,
    fields: List[str],
    data: Dict[str, Any]
) -> Tuple[DjangoModelType, bool]:
    """
    Generic update service meant to be reused in local update services

    For example:

    def user_update(*, user: User, data) -> User:
        fields = ['first_name', 'last_name']
        user, has_updated = model_update(instance=user, fields=fields, data=data)

        // Do other actions with the user here

        return user

    Return value: Tuple with the following elements:
        1. The instance we updated
        2. A boolean value representing whether we performed an update or not.
    """
    has_updated = False

    for field in fields:
        # Skip if a field is not present in the actual data
        if field not in data:
            continue

        if getattr(instance, field) != data[field]:
            has_updated = True
            setattr(instance, field, data[field])

    # Perform an update only if any of the fields was actually changed
    if has_updated:
        instance.full_clean()
        # Update only the fields that are meant to be updated.
        # Django docs reference:
        # https://docs.djangoproject.com/en/dev/ref/models/instances/#specifying-which-fields-to-save
        instance.save(update_fields=fields)

    return instance, has_updated


def model_delete(
    *,
    instance: DjangoModelType,
) -> None:

    data = {'removed': True}
    fields = ['removed', ]

    model_update(
        instance=instance,
        fields=fields,
        data=data
    )


@transaction.atomic
def generic_model_update(
    *,
    instance: DjangoModelType,
    data: Dict[str, Any]
) -> DjangoModelType:
    model_fields = list(vars(instance).keys())
    model_fields.remove('id')

    for field in model_fields:
        if field == '_state':
            model_fields.remove('_state')

        if field.endswith('_id'):
            modified_field = field[:-3]
            model_fields.remove(field)
            model_fields.append(modified_field)

    if not instance:
        INSTANCE_IS_NONE = f'You attempted updating a \
            {instance.__class__.__name__} that does not exist!'
        raise ValidationError(INSTANCE_IS_NONE)

    _employee, has_updated = model_update(
        instance=instance,
        fields=model_fields,
        data=data
    )

    return _employee
