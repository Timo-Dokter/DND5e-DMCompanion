from django.db import models
from django.utils.translation import gettext_lazy as _


class ItemTrait(models.Model):
    """
    Model for ItemTrait
    """

    item = models.ForeignKey(
        "item.Item", on_delete=models.CASCADE, related_name="traits"
    )
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = _("Item Trait")
        verbose_name_plural = _("Item Traits")

    def __str__(self):
        return f"{self.item} - {self.name}"
