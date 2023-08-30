from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Tavern(Building):
    type = "Tavern"
    employees = models.ManyToManyField(
        "character.Character",
        related_name="taverns",
        blank=True,
    )
    rooms = models.ManyToManyField(
        "character.Character",
        related_name="taverns",
        blank=True,
    )

    class Meta:
        verbose_name = _("Tavern")
        verbose_name_plural = _("Taverns")

    def __str__(self):
        return self.name
