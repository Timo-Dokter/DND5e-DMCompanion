from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Fort(Building):
    type = "Fort"
    soldiers = models.ManyToManyField(
        "character.Character",
        related_name="forts",
        blank=True,
    )

    class Meta:
        verbose_name = _("Fort")
        verbose_name_plural = _("Forts")

    def __str__(self):
        return self.name
