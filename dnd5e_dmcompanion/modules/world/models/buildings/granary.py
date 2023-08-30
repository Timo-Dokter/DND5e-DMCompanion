from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Granary(Building):
    type = "Granary"
    items = models.ManyToManyField(
        "item.Item",
        related_name="granaries",
        blank=True,
    )

    class Meta:
        verbose_name = _("Granary")
        verbose_name_plural = _("Granaries")

    def __str__(self):
        return self.name
