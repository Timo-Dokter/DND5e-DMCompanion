from django.db import models
from django.utils.translation import gettext_lazy as _

from ..building import Building


class GuardPost(Building):
    type = "Guard Post"
    guards = models.ManyToManyField(
        "character.Character",
        related_name="guard_posts",
        blank=True,
    )

    class Meta:
        verbose_name = _("Guard Post")
        verbose_name_plural = _("Guard Posts")
