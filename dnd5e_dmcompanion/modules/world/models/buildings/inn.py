from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Inn(Building):
    type = "Inn"
    employees = models.ManyToManyField(
        "character.Character",
        related_name="inns_employees",
        blank=True,
    )
    rooms = models.ManyToManyField(
        "character.Character",
        related_name="inns_rooms",
        blank=True,
    )

    class Meta:
        verbose_name = _("Inn")
        verbose_name_plural = _("Inns")

    def __str__(self):
        return self.name
