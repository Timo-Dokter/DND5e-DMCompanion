from django.db import models
from django.utils.translation import gettext_lazy as _


class ItemModifier(models.Model):
    """
    Model for ItemModifier
    """

    MODIFIER_TYPES = (
        ("bonus", _("Bonus")),
        ("penalty", _("Penalty")),
    )

    modifies = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    type = models.CharField(max_length=255, choices=MODIFIER_TYPES)
    item = models.OneToOneField(
        "item.Item", on_delete=models.CASCADE, related_name="modifier"
    )

    class Meta:
        verbose_name = _("Item Modifier")
        verbose_name_plural = _("Item Modifiers")

    def __str__(self):
        return f"{self.item} - {self.modifies} {self.type} {self.amount}"
