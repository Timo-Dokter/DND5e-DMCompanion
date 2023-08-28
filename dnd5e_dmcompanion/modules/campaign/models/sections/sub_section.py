from django.db import models
from django.utils.translation import gettext_lazy as _

from ...models import BaseSection


class SubSection(BaseSection):
    parent = models.ForeignKey(
        "campaign.BaseSection",
        verbose_name=_("Section"),
        on_delete=models.CASCADE,
        related_name="sub_sections",
    )

    class Meta:
        verbose_name = _("Sub Section")
        verbose_name_plural = _("Sub Sections")
