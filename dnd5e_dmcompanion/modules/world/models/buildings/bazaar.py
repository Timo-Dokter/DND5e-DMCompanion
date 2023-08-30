from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Bazaar(Building):
    type = "Bazaar"
    items = models.ManyToManyField(
        "item.Item",
        related_name="bazaars",
        blank=True,
    )

    class Meta:
        verbose_name = _("Bazaar")
        verbose_name_plural = _("Bazaars")

    def __str__(self):
        return self.name
