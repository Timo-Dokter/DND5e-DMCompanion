from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Workshop(Building):
    type = "Workshop"
    employees = models.ManyToManyField(
        "character.Character",
        related_name="workshops",
        blank=True,
    )
    items = models.ManyToManyField(
        "item.Item",
        related_name="workshops",
        blank=True,
    )

    class Meta:
        verbose_name = _("Workshop")
        verbose_name_plural = _("Workshops")

    def __str__(self):
        return self.name
