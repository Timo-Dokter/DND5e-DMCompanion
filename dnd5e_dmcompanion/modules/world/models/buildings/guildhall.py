from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Guildhall(Building):
    type = "Guildhall"
    guildmasters = models.ManyToManyField(
        "character.Character",
        related_name="guildhalls",
        blank=True,
    )

    class Meta:
        verbose_name = _("Guildhall")
        verbose_name_plural = _("Guildhalls")

    def __str__(self):
        return self.name
