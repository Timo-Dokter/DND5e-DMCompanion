from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Church(Building):
    type = "Church"
    priests = models.ManyToManyField(
        "character.Character",
        related_name="churches",
        blank=True,
    )

    class Meta:
        verbose_name = _("Church")
        verbose_name_plural = _("Churches")

    def __str__(self):
        return self.name
