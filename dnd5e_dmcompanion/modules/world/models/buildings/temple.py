from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Temple(Building):
    type = "Temple"
    gods = models.ManyToManyField(
        "character.Character",
        related_name="temples",
        blank=True,
    )

    class Meta:
        verbose_name = _("Temple")
        verbose_name_plural = _("Temples")

    def __str__(self):
        return self.name
