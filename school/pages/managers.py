from django.db import models

class PageManager(models.Manager):
    def published(self, *args, **kwargs):
        qs = super(PageManager, self).all(*args, **kwargs)
        return qs.filter(is_published=True)
