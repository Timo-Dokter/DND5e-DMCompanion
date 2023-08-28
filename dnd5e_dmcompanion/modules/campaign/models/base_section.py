from django.db import models
from django.utils.translation import gettext_lazy as _
from django_bleach.models import BleachField
from polymorphic.models import PolymorphicModel


class BaseSection(PolymorphicModel):
    name = models.CharField(_("Name"), max_length=255)

    text = BleachField(_("Description"), blank=True, null=True)

    class Meta:
        verbose_name = _("Base Section")
        verbose_name_plural = _("Base Sections")
        ordering = ("name",)

    def __str__(self):
        return self.name
