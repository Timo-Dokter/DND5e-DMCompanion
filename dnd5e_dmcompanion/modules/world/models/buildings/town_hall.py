from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class TownHall(Building):
    type = "TownHall"
    employees = models.ManyToManyField(
        "character.Character",
        related_name="town_halls_employees",
        blank=True,
    )
    rooms = models.ManyToManyField(
        "character.Character",
        related_name="town_halls_rooms",
        blank=True,
    )

    class Meta:
        verbose_name = _("TownHall")
        verbose_name_plural = _("TownHalls")

    def __str__(self):
        return self.name
