from django.db import models
from django.utils.translation import gettext_lazy as _


class Mineral(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    description = models.TextField(
        verbose_name=_("Description"),
    )

    class Meta:
        verbose_name = _("Mineral")
        verbose_name_plural = _("Minerals")

    def __str__(self):
        return self.name
