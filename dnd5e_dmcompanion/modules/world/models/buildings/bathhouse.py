from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Bathhouse(Building):
    type = "Bathhouse"
    employees = models.ManyToManyField(
        "character.Character",
        related_name="bathhouses_employees",
        blank=True,
    )
    rooms = models.ManyToManyField(
        "character.Character",
        related_name="bathhouses_rooms",
        blank=True,
    )

    class Meta:
        verbose_name = _("Bathhouse")
        verbose_name_plural = _("Bathhouses")

    def __str__(self):
        return self.name
