from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Quarry(Building):
    type = "Quarry"
    mineral = models.ForeignKey(
        "world.Mineral",
        related_name="quarries",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Quarry")
        verbose_name_plural = _("Quarries")

    def __str__(self):
        return self.name
