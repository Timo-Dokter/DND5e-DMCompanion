from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Mansion(Building):
    type = "Mansion"
    residents = models.ManyToManyField(
        "character.Character",
        related_name="mansions",
        blank=True,
    )

    class Meta:
        verbose_name = _("Mansion")
        verbose_name_plural = _("Mansions")

    def __str__(self):
        return self.name
