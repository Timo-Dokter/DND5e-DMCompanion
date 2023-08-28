from django.db import models
from django.utils.translation import gettext_lazy as _


class ItemProperty(models.Model):
    """
    Model for ItemProperty
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Item Property")
        verbose_name_plural = _("Item Properties")

    def __str__(self):
        return self.name
