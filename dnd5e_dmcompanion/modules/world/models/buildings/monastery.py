from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Monastery(Building):
    type = "Monastery"
    monks = models.ManyToManyField(
        "character.Character",
        related_name="monasteries",
        blank=True,
    )

    class Meta:
        verbose_name = _("Monastery")
        verbose_name_plural = _("Monasteries")

    def __str__(self):
        return self.name
