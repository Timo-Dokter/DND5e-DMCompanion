from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Mill(Building):
    type = "Mill"
    workers = models.ManyToManyField(
        "character.Character",
        related_name="mills",
        blank=True,
    )

    class Meta:
        verbose_name = _("Mill")
        verbose_name_plural = _("Mills")

    def __str__(self):
        return self.name
