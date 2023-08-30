from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Monument(Building):
    type = "Monument"

    class Meta:
        verbose_name = _("Monument")
        verbose_name_plural = _("Monuments")

    def __str__(self):
        return self.name
