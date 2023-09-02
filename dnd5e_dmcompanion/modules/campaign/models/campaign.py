from django.db import models
from django.utils.translation import gettext_lazy as _
from django_bleach.models import BleachField


class Campaign(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    introduction = BleachField(_("Introduction"), blank=True, null=True)
    featured_image = models.ImageField(
        _("Featured Image"), upload_to="campaigns/", blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Campaign")
        verbose_name_plural = _("Campaigns")
