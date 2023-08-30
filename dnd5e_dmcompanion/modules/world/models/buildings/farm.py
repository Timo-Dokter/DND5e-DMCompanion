from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Farm(Building):
    type = "Farm"
    workers = models.ManyToManyField(
        "character.Character",
        related_name="farms",
        blank=True,
    )

    class Meta:
        verbose_name = _("Farm")
        verbose_name_plural = _("Farms")

    def __str__(self):
        return self.name
