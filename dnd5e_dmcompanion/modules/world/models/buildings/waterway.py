from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Waterway(Building):
    type = "Waterway"

    class Meta:
        verbose_name = _("Waterway")
        verbose_name_plural = _("Waterways")

    def __str__(self):
        return self.name
