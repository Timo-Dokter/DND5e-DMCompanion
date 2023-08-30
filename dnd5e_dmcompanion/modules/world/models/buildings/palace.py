from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Palace(Building):
    type = "Palace"
    nobles = models.ManyToManyField(
        "character.Character",
        related_name="palaces",
        blank=True,
    )

    class Meta:
        verbose_name = _("Palace")
        verbose_name_plural = _("Palaces")

    def __str__(self):
        return self.name
