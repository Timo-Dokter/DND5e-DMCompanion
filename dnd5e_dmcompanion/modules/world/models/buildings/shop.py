from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Shop(Building):
    type = "Shop"
    employees = models.ManyToManyField(
        "character.Character",
        related_name="shops",
        blank=True,
    )
    shop_type = models.CharField(max_length=255, blank=True, null=True)
    items = models.ManyToManyField(
        "item.Item",
        related_name="shops",
        blank=True,
    )

    class Meta:
        verbose_name = _("Shop")
        verbose_name_plural = _("Shops")
