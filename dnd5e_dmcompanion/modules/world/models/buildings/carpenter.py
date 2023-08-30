from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Carpenter(Building):
    type = "Carpenter"
    items = models.ManyToManyField(
        "item.Item",
        related_name="carpenters",
        blank=True,
    )

    class Meta:
        verbose_name = _("Carpenter")
        verbose_name_plural = _("Carpenters")

    def __str__(self):
        return self.name
