from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Windmill(Building):
    type = "Windmill"

    class Meta:
        verbose_name = _("Windmill")
        verbose_name_plural = _("Windmills")

    def __str__(self):
        return self.name
