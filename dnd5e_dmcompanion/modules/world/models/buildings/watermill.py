from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Watermill(Building):
    type = "Watermill"

    class Meta:
        verbose_name = _("Watermill")
        verbose_name_plural = _("Watermills")

    def __str__(self):
        return self.name
