from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Shrine(Building):
    type = "Shrine"

    class Meta:
        verbose_name = _("Shrine")
        verbose_name_plural = _("Shrines")

    def __str__(self):
        return self.name
