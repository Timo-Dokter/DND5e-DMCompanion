from django.db import models
from django.utils.translation import gettext_lazy as _
from django_bleach.models import BleachField


class Overview(models.Model):
    campaign = models.OneToOneField(
        "campaign.Campaign", verbose_name=_("Campaign"), on_delete=models.CASCADE
    )
    description = BleachField(_("Description"), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Overview")
        verbose_name_plural = _("Overviews")
