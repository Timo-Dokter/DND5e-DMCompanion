from django.db import models
from django.utils.translation import gettext_lazy as _
from django_bleach.models import BleachField
from polymorphic.models import PolymorphicModel


class ImportantNote(PolymorphicModel):
    title = models.CharField(_("Title"), max_length=255, blank=True, null=True)
    content = BleachField(_("Content"), blank=True, null=True)

    class Meta:
        verbose_name = _("Important Note Section")
        verbose_name_plural = _("Important Note Sections")

    def __str__(self):
        return self.title
