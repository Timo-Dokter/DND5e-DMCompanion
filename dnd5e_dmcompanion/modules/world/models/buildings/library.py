from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class Library(Building):
    type = "Library"
    books = models.ManyToManyField(
        "item.Item",
        related_name="libraries",
        blank=True,
    )

    class Meta:
        verbose_name = _("Library")
        verbose_name_plural = _("Libraries")
