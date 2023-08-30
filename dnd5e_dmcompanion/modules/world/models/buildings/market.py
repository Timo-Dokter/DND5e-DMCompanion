from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Market(Building):
    type = "Market"
    items = models.ManyToManyField(
        "item.Item",
        related_name="markets",
        blank=True,
    )

    class Meta:
        verbose_name = _("Market")
        verbose_name_plural = _("Markets")

    def __str__(self):
        return self.name
