from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Gatehouse(Building):
    type = "Gatehouse"
    guards = models.ManyToManyField(
        "character.Character",
        related_name="gatehouses",
        blank=True,
    )

    class Meta:
        verbose_name = _("Gatehouse")
        verbose_name_plural = _("Gatehouses")

    def __str__(self):
        return self.name
