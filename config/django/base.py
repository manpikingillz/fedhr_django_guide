'''
Django settings for fedhr project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
'''

import os

from config.env import env, BASE_DIR

env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=ug_ucl@yi6^mrcjyz%(u0%&g2adt#bz3@yos%#@*t#t!ypx=a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

LOCAL_APPS = [
    'fedhr.core.apps.CoreConfig',
    'fedhr.common.apps.CommonConfig',
    'fedhr.tasks.apps.TasksConfig',
    'fedhr.api.apps.ApiConfig',
    'fedhr.users.apps.UsersConfig',
    'fedhr.errors.apps.ErrorsConfig',
    'fedhr.testing_examples.apps.TestingExamplesConfig',
    'fedhr.integrations.apps.IntegrationsConfig',
    'fedhr.files.apps.FilesConfig',
    'fedhr.emails.apps.EmailsConfig',
    'fedhr.setup.apps.SetupConfig',
    'fedhr.employee.apps.EmployeeConfig',
    'fedhr.hiring.apps.HiringConfig',
    'fedhr.timeoff.apps.TimeoffConfig',
    'fedhr.scheduling.apps.SchedulingConfig',
    'fedhr.payroll.apps.PayrollConfig',
    'fedhr.timesheet.apps.TimesheetConfig',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_celery_results',
    'django_celery_beat',
    'django_filters',
    'corsheaders',
    'django_extensions',
    'rest_framework_jwt',
    'graphene_django',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    'graphql_auth',
]

INSTALLED_APPS = [
    'jazzmin',  # Must be added before 'django.contrib.admin'

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres:///fedhr'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

if os.environ.get('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'github_actions',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'users.BaseUser'


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

REST_FRAMEWORK = {
    # 'EXCEPTION_HANDLER': 'fedhr.api.exception_handlers.drf_default_with_modifications_exception_handler',
    'EXCEPTION_HANDLER': 'fedhr.api.exception_handlers.hacksoft_proposed_exception_handler',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': []
}

APP_DOMAIN = env('APP_DOMAIN', default='http://localhost:8000')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ADMIN_SITE_HEADER = 'FedHR'


JAZZMIN_SETTINGS = {
    'show_ui_builder': True,
    # 'order_with_respect_to': ['employee', 'hiring'],
    'order_with_respect_to': [
        # order of apps
        'employee', 'hiring', 'timeoff', 'scheduling', 'payroll', 'timesheet',

        # order of employee models
        'employee.Employee',
        'employee.JobInformation', 'employee.Education',
        'employee.EmploymentStatus', 'employee.VisaInformation',
        'employee.Compensation', 'employee.EmergencyContact',
        'employee.Dependant', 'employee.Note',

        # order of hiring models
        'hiring.JobOpening',
        'hiring.Candidate',
        'hiring.JobApplication',
        'hiring.QuestionType',
        'hiring.Question',
        'hiring.JobOpeningQuestion',
        'hiring.ApplicationStatus',
        'hiring.JobApplicationQuestion',
        'hiring.JobApplicationQuestionAnswer',
        'hiring.JobApplicationEmail',
        'hiring.JobApplicationComment',
        'hiring.TalentPool',
        'hiring.TalentPoolApplicant',

        # order of timeoff models
        'timeoff.LeaveCategory',
        'timeoff.LeavePolicy',
        'timeoff.AccrualMilestone',
        'timeoff.Holiday',
        'timeoff.WorkWeek',

        # order of payroll models
        'payroll.EmployeePayroll',
        'payroll.PayrollPeriod',

        # order of timesheet models
        'timesheet.TimeRecord',
        'timesheet.Task'
    ],

    'topmenu_links': [

        # Url that gets reversed (Permissions can be added)
        {'name': 'Home',  'url': 'admin:index', 'permissions': ['auth.view_user']},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {'app': 'employee'},
        {'app': 'hiring'},
        {'app': 'timeoff'},
        {'app': 'scheduling'},
        {'app': 'payroll'},
        {'app': 'timesheet'},
    ],
    'search_model': ['employee.Employee', ],
    'welcome_sign': 'Welcome to FedHR',
    'changeform_format': 'vertical_tabs'
}

JAZZMIN_UI_TWEAKS = {
    'navbar_small_text': False,
    'footer_small_text': False,
    'body_small_text': False,
    'brand_small_text': False,
    'brand_colour': 'navbar-primary',
    'accent': 'accent-primary',
    'navbar': 'navbar-primary navbar-dark',
    'no_navbar_border': False,
    'navbar_fixed': False,
    'layout_boxed': False,
    'footer_fixed': False,
    'sidebar_fixed': False,
    'sidebar': 'sidebar-dark-primary',
    'sidebar_nav_small_text': False,
    'sidebar_disable_expand': False,
    'sidebar_nav_child_indent': False,
    'sidebar_nav_compact_style': False,
    'sidebar_nav_legacy_style': False,
    'sidebar_nav_flat_style': False,
    'theme': 'default',
    'dark_mode_theme': None,
    'button_classes': {
        'primary': 'btn-primary',
        'secondary': 'btn-secondary',
        'info': 'btn-info',
        'warning': 'btn-warning',
        'danger': 'btn-danger',
        'success': 'btn-success'
    }
}

GRAPHENE = {
    "SCHEMA": "fedhr.graphql_schema.schema",
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ]
}

AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    "graphql_auth.backends.GraphQLAuthBackend",
    'django.contrib.auth.backends.ModelBackend',
]

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,

    # optional
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,

    "JWT_ALLOW_ANY_CLASSES": [
        "graphql_auth.mutations.Register",
        "graphql_auth.mutations.VerifyAccount",
        "graphql_auth.mutations.ObtainJSONWebToken"
    ],
}

from config.settings.cors import *  # noqa
from config.settings.jwt import *  # noqa
from config.settings.sessions import *  # noqa
from config.settings.celery import *  # noqa
from config.settings.sentry import *  # noqa

from config.settings.files_and_storages import *  # noqa
from config.settings.email_sending import *  # noqa
