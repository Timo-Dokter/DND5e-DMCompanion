from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Tenement(Building):
    type = "Tenement"

    class Meta:
        verbose_name = _("Tenement")
        verbose_name_plural = _("Tenements")

    def __str__(self):
        return self.name
