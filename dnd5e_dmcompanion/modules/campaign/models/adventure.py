from django.db import models
from django.utils.translation import gettext_lazy as _
from django_bleach.models import BleachField


class Adventure(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    campaign = models.ForeignKey(
        "campaign.Campaign",
        verbose_name=_("Campaign"),
        on_delete=models.CASCADE,
        related_name="adventures",
    )
    short_description = BleachField(_("Introduction"), blank=True, null=True)

    class Meta:
        verbose_name = _("Adventure")
        verbose_name_plural = _("Adventures")

    def __str__(self):
        return self.name
