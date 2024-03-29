from django.contrib import admin, messages
from django.core.exceptions import ValidationError

from fedhr.users.models import BaseUser
from fedhr.users.services import user_create


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_admin', 'is_superuser', 'is_active', 'created_at', 'updated_at',)

    search_fields = ('email',)

    list_filter = ('is_active', 'is_admin', 'is_superuser')

    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (
            None, {
                'fields': ('email', 'username', 'first_name', 'last_name')
            }
        ),
        (
            "Booleans", {
                "fields": ("is_active", "is_admin", "is_superuser")
            }
        ),
        (
            "Groups and Permissions", {
                "fields": ('groups', 'user_permissions',)
            }
        ),
        (
            "Timestamps", {
                "fields": ("created_at", "updated_at")
            }
        )
    )

    readonly_fields = ("created_at", "updated_at", )

    # Commented out so that we can use the built in methods.
    # Also, it was not straightfoward how to save groups
    # and user_permissions. Editing was fine though.

    # def save_model(self, request, obj, form, change):
    #     if change:
    #         return super().save_model(request, obj, form, change)

    #     try:
    #         user_create(**form.cleaned_data)
    #     except ValidationError as exc:
    #         self.message_user(request, str(exc), messages.ERROR)
