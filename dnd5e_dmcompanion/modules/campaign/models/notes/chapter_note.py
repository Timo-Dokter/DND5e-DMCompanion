from django.db import models
from django.utils.translation import gettext_lazy as _

from ...models import ImportantNote


class ChapterNote(ImportantNote):
    parent = models.ForeignKey(
        "campaign.Chapter",
        verbose_name=_("Chapter"),
        on_delete=models.CASCADE,
        related_name="notes",
    )

    class Meta:
        verbose_name = _("Chapter Note")
        verbose_name_plural = _("Chapter Notes")
