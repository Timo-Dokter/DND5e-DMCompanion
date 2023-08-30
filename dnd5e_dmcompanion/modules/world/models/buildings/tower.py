from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Tower(Building):
    type = "Tower"

    class Meta:
        verbose_name = _("Tower")
        verbose_name_plural = _("Towers")

    def __str__(self):
        return self.name
