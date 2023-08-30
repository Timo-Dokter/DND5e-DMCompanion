from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Watchtower(Building):
    type = "Watchtower"

    class Meta:
        verbose_name = _("Watchtower")
        verbose_name_plural = _("Watchtowers")

    def __str__(self):
        return self.name
