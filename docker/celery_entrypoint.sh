echo "--> Starting celery process"
celery -A fedhr.tasks beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler