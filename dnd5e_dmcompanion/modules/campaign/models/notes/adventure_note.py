from django.db import models
from django.utils.translation import gettext_lazy as _

from ...models import ImportantNote


class AdventureNote(ImportantNote):
    parent = models.ForeignKey(
        "campaign.Adventure",
        verbose_name=_("Adventure"),
        on_delete=models.CASCADE,
        related_name="notes",
    )

    class Meta:
        verbose_name = _("Adventure Note")
        verbose_name_plural = _("Adventure Notes")
