from django.db import models
from .choices import FOOTER_MENU_POSITION, TOP_MENU_POSITION

class MenuManager(models.Manager):
    def footer(self, *args, **kwargs):
        qs = super(MenuManager, self).all(*args, **kwargs)
        return qs.filter(position=FOOTER_MENU_POSITION)

    def top(self, *args, **kwargs):
        qs = super(MenuManager, self).all(*args, **kwargs)
        return qs.filter(position=TOP_MENU_POSITION)
