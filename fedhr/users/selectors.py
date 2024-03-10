from django.db.models.query import QuerySet

from fedhr.users.models import BaseUser
from fedhr.users.filters import BaseUserFilter


def user_get_login_data(*, user: BaseUser):
    return {
        'id': user.id,
        'full_name': user.full_name(),
        'email': user.email,
        'is_active': user.is_active,
        'is_admin': user.is_admin,
        'is_superuser': user.is_superuser,
        'permissions': user.get_all_permissions(),
        'groups': user.groups.all().values_list('name', flat=True)
    }


def user_list(*, filters=None) -> QuerySet[BaseUser]:
    filters = filters or {}

    qs = BaseUser.objects.all()

    return BaseUserFilter(filters, qs).qs
