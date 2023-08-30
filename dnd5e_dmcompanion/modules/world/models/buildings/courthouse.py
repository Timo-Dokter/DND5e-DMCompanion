from django.db import models
from django.utils.translation import gettext_lazy as _


from ..building import Building


class Courthouse(Building):
    type = "Courthouse"
    judges = models.ManyToManyField(
        "character.Character",
        related_name="courthouses",
        blank=True,
    )

    class Meta:
        verbose_name = _("Courthouse")
        verbose_name_plural = _("Courthouses")

    def __str__(self):
        return self.name
