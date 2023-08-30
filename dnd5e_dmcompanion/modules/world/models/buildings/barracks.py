from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Barracks(Building):
    type = "Barracks"
    soldiers = models.ManyToManyField(
        "character.Character",
        related_name="barracks",
        blank=True,
    )

    class Meta:
        verbose_name = _("Barracks")
        verbose_name_plural = _("Barracks")

    def __str__(self):
        return self.name
