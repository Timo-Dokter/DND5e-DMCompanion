from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Stable(Building):
    type = "Stable"

    class Meta:
        verbose_name = _("Stable")
        verbose_name_plural = _("Stables")

    def __str__(self):
        return self.name
