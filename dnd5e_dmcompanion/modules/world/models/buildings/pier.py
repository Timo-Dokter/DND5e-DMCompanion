from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Pier(Building):
    type = "Pier"
    ships = models.ManyToManyField(
        "world.Ship",
        related_name="piers",
        blank=True,
    )

    class Meta:
        verbose_name = _("Pier")
        verbose_name_plural = _("Piers")

    def __str__(self):
        return self.name
