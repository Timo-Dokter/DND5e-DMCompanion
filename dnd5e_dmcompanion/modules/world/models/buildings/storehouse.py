from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Storehouse(Building):
    type = "Storehouse"

    class Meta:
        verbose_name = _("Storehouse")
        verbose_name_plural = _("Storehouses")

    def __str__(self):
        return self.name
