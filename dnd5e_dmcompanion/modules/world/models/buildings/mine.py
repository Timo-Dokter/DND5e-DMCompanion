from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Mine(Building):
    type = "Mine"
    workers = models.ManyToManyField(
        "character.Character",
        related_name="mines",
        blank=True,
    )

    class Meta:
        verbose_name = _("Mine")
        verbose_name_plural = _("Mines")

    def __str__(self):
        return self.name
