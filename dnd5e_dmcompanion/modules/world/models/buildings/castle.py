from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Castle(Building):
    type = "Castle"
    nobles = models.ManyToManyField(
        "character.Character",
        related_name="castles_nobles",
        blank=True,
    )
    soldiers = models.ManyToManyField(
        "character.Character",
        related_name="castles_soldiers",
        blank=True,
    )

    class Meta:
        verbose_name = _("Castle")
        verbose_name_plural = _("Castles")

    def __str__(self):
        return self.name
