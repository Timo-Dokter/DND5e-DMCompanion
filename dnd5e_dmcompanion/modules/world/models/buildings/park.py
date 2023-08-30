from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Park(Building):
    type = "Park"
    visitors = models.ManyToManyField(
        "character.Character",
        related_name="parks",
        blank=True,
    )

    class Meta:
        verbose_name = _("Park")
        verbose_name_plural = _("Parks")

    def __str__(self):
        return self.name
