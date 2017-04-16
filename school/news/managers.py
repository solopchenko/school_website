from django.db import models

class ArticleManager(models.Manager):
    def published(self, *args, **kwargs):
        qs = super(ArticleManager, self).all(*args, **kwargs)
        return qs.filter(published=True)
