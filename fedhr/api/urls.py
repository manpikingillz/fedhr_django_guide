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
    path('educations/', include(('fedhr.employee.urls_education', 'educations'))),
    path('visa-informations/', include(('fedhr.employee.urls_visa_information', 'visa_informations'))),
    path('employment-status/', include(('fedhr.employee.urls_employment_status', 'employment_status'))),
    path('job-information/', include(('fedhr.employee.urls_job_information', 'job_information'))),
    path('compensation/', include(('fedhr.employee.urls_compensation', 'compensation'))),
    path('emergency-contact/', include(('fedhr.employee.urls_emergency_contact', 'emergency_contact'))),
    path('asset/', include(('fedhr.employee.urls_asset', 'asset'))),
    path('training/', include(('fedhr.employee.urls_training', 'training'))),
    path('template/', include(('fedhr.hiring.urls', 'template')))
]
