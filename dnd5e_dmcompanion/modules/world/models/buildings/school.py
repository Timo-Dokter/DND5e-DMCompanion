from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class School(Building):
    type = "School"

    class Meta:
        verbose_name = _("School")
        verbose_name_plural = _("Schools")

    def __str__(self):
        return self.name
