from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class University(Building):
    type = "University"

    class Meta:
        verbose_name = _("University")
        verbose_name_plural = _("Universities")

    def __str__(self):
        return self.name
