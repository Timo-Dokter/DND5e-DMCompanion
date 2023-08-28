from django.db import models
from django.utils.translation import gettext_lazy as _

from ...models import BaseSection


class ChapterSection(BaseSection):
    parent = models.ForeignKey(
        "campaign.Chapter",
        verbose_name=_("Chapter"),
        on_delete=models.CASCADE,
        related_name="sections",
    )

    class Meta:
        verbose_name = _("Chapter Section")
        verbose_name_plural = _("Chapter Sections")
