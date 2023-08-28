from django.db import models
from django.utils.translation import gettext_lazy as _

from ...models import BaseSection


class OverviewSection(BaseSection):
    parent = models.ForeignKey(
        "campaign.Overview",
        verbose_name=_("Overview"),
        on_delete=models.CASCADE,
        related_name="sections",
    )

    class Meta:
        verbose_name = _("Overview Section")
        verbose_name_plural = _("Overview Sections")
