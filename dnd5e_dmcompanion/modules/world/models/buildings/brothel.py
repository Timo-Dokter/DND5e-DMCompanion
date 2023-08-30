from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Brothel(Building):
    type = "Brothel"
    prostitutes = models.ManyToManyField(
        "character.Character",
        related_name="brothels",
        blank=True,
    )

    class Meta:
        verbose_name = _("Brothel")
        verbose_name_plural = _("Brothels")

    def __str__(self):
        return self.name
