from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Lumberyard(Building):
    type = "Lumberyard"
    lumberjacks = models.ManyToManyField(
        "character.Character",
        related_name="lumberyards",
        blank=True,
    )

    class Meta:
        verbose_name = _("Lumberyard")
        verbose_name_plural = _("Lumberyards")

    def __str__(self):
        return self.name
