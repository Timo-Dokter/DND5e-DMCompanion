from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Lighthouse(Building):
    type = "Lighthouse"
    keepers = models.ManyToManyField(
        "character.Character",
        related_name="lighthouses",
        blank=True,
    )

    class Meta:
        verbose_name = _("Lighthouse")
        verbose_name_plural = _("Lighthouses")

    def __str__(self):
        return self.name
