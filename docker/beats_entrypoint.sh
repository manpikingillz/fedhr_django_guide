echo "--> Starting beats process"
celery -A fedhr.tasks worker -l info --without-gossip --without-mingle --without-heartbeat