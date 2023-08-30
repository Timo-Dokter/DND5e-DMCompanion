from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Warehouse(Building):
    type = "Warehouse"
    items = models.ManyToManyField(
        "item.Item",
        related_name="warehouses",
        blank=True,
    )

    class Meta:
        verbose_name = _("Warehouse")
        verbose_name_plural = _("Warehouses")

    def __str__(self):
        return self.name
