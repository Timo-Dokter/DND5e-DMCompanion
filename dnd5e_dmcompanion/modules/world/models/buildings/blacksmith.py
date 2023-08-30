from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Blacksmith(Building):
    type = "Blacksmith"
    employees = models.ManyToManyField(
        "character.Character",
        related_name="blacksmiths",
        blank=True,
    )
    items = models.ManyToManyField(
        "item.Item",
        related_name="blacksmiths",
        blank=True,
    )

    class Meta:
        verbose_name = _("Blacksmith")
        verbose_name_plural = _("Blacksmiths")

    def __str__(self):
        return self.name
