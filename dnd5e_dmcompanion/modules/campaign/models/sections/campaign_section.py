from django.db import models
from django.utils.translation import gettext_lazy as _

from ...models import BaseSection


class CampaignSection(BaseSection):
    parent = models.ForeignKey(
        "campaign.Campaign",
        verbose_name=_("Campaign"),
        on_delete=models.CASCADE,
        related_name="sections",
    )

    class Meta:
        verbose_name = _("Campaign Section")
        verbose_name_plural = _("Campaign Sections")
