from django.db import models
from django.utils.translation import gettext_lazy as _


class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Position")
        verbose_name_plural = _("Positions")
