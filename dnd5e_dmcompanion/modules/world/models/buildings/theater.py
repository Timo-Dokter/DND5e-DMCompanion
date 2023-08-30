from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Theater(Building):
    type = "Theater"

    class Meta:
        verbose_name = _("Theater")
        verbose_name_plural = _("Theaters")

    def __str__(self):
        return self.name
