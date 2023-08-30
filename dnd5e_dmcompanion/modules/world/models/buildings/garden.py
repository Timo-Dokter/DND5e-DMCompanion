from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Garden(Building):
    type = "Garden"
    gardeners = models.ManyToManyField(
        "character.Character",
        related_name="gardens",
        blank=True,
    )

    class Meta:
        verbose_name = _("Garden")
        verbose_name_plural = _("Gardens")

    def __str__(self):
        return self.name
