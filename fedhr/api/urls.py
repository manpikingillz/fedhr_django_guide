from django.urls import path, include
from django.conf import settings
from django.contrib import admin

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    path(
        'auth/', include(('fedhr.authentication.urls', 'authentication'))
    ),
    path('users/', include(('fedhr.users.urls', 'users'))),
    path('errors/', include(('fedhr.errors.urls', 'errors'))),
    path('files/', include(('fedhr.files.urls', 'files'))),
    path('setup/', include(('fedhr.setup.urls', 'setup'))),
    path('employees/', include(('fedhr.employee.urls', 'employees'))),
    path('notes/', include(('fedhr.employee.urls_notes', 'notes'))),
]
