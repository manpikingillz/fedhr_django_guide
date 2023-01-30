from typing import Optional

from django.db import transaction

from fedhr.common.services import model_update

from fedhr.users.models import BaseUser


def user_create(
    *,
    first_name: str,
    last_name: str,
    username: str,
    email: str,
    is_superuser: bool,
    is_active: bool = True,
    is_admin: bool = False,
    password: Optional[str] = None,
    **extra_fields
) -> BaseUser:
    user = BaseUser.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        is_superuser=is_superuser,
        is_active=is_active,
        is_admin=is_admin,
        password=password,
        **extra_fields
    )

    return user


@transaction.atomic
def user_update(*, user: BaseUser, data) -> BaseUser:
    non_side_effect_fields = ['first_name', 'last_name']

    user, has_updated = model_update(
        instance=user,
        fields=non_side_effect_fields,
        data=data
    )

    # Side-effect fields update here (e.g. username is generated based on first & last name)

    # ... some additional tasks with the user ...

    return user
