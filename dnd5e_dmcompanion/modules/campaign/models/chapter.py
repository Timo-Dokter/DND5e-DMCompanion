from django.db import models
from django.utils.translation import gettext_lazy as _
from django_bleach.models import BleachField


class Chapter(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    adventure = models.ForeignKey(
        "campaign.Adventure",
        verbose_name=_("Adventure"),
        on_delete=models.CASCADE,
        related_name="chapters",
    )
    description = BleachField(_("Description"), blank=True, null=True)
    number = models.PositiveIntegerField(_("Number"), default=1)

    class Meta:
        verbose_name = _("Chapter")
        verbose_name_plural = _("Chapters")
        unique_together = (("adventure", "number"),)
        ordering = ("number",)

    def __str__(self):
        return self.name
