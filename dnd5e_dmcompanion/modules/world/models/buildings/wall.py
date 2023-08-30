from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Wall(Building):
    type = "Wall"

    class Meta:
        verbose_name = _("Wall")
        verbose_name_plural = _("Walls")

    def __str__(self):
        return self.name
