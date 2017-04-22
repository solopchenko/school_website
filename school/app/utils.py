from django.conf import settings
from datetime import datetime
from django.utils import timezone

def get_now():
    if settings.USE_TZ:
        return datetime.utcnow().replace(tzinfo=timezone.utc)
    else:
        return datetime.now()
