from django.db import models

class CategoryManager(models.Manager):
    def public(self, *args, **kwargs):
        qs = super(CategoryManager, self).all(*args, **kwargs)
        return qs.filter(is_public=True)

    def private(self, *args, **kwargs):
        qs = super(CategoryManager, self).all(*args, **kwargs)
        return qs.filter(is_public=False)
